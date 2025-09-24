import datetime
import logging
import torch
from pathlib import Path
import sys
from torch import nn
from torch.utils.data import DataLoader
from ideeplc.model import MyNet
from ideeplc.config import get_config
from ideeplc.data_initialize import data_initialize
from ideeplc.predict import predict
from ideeplc.figure import make_figures
from ideeplc.fine_tuning import iDeepLCFineTuner
from importlib.resources import files

# Logging configuration
LOGGER = logging.getLogger(__name__)


def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(log_dir / "ideeplc.log")
    console_handler = logging.StreamHandler()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[file_handler, console_handler],
    )


setup_logging()


def get_model_save_path():
    """
    Determines the correct directory and filename for saving the model.
    Appends a timestamp to the filename to prevent overwriting.


    Returns:
        tuple: (model_save_path, model_dir)
    """
    timestamp = datetime.datetime.now().strftime("%m%d")
    model_dir = Path("ideeplc/models") / timestamp
    model_name = "pretrained_model.pth"

    if getattr(sys, "frozen", False):
        # If frozen (PyInstaller)
        base_path = Path(sys._MEIPASS)
        model_path = base_path / "ideeplc" / "models" / model_name
    else:
        # If normal Python environment
        model_path = files("ideeplc.models").joinpath(model_name)

    return model_path, model_dir


def main(args):
    """
    Main function that executes training/evaluation for the iDeepLC package based on the provided arguments.

    Args:
        args (argparse.Namespace): Parsed arguments from the CLI.
    """

    LOGGER.info("Starting iDeepLC prediction...")
    try:
        # Load configuration
        config = get_config()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Initialize data
        LOGGER.info(f"Loading data from {args.input}")
        matrix_input, x_shape = data_initialize(csv_path=args.input)
        # Initialize model
        LOGGER.info("Initializing model")
        model = MyNet(x_shape=x_shape, config=config).to(device)

        # Load pre-trained model
        LOGGER.info("Loading pre-trained model")
        pretrained_model, model_dir = get_model_save_path()
        if args.model:
            try:
                logging.info(f"Using user-specified model path: {args.model}")
                pretrained_model = Path(args.model)
            except Exception as e:
                LOGGER.error(f"Invalid model path provided: {e}")
                raise e
        model.load_state_dict(
            torch.load(pretrained_model, map_location=device), strict=False
        )
        loss_function = nn.L1Loss()

        if args.finetune:
            LOGGER.info("Fine-tuning the model")
            fine_tuner = iDeepLCFineTuner(
                model=model,
                train_data=matrix_input,
                loss_function=loss_function,
                device=device,
                learning_rate=config["learning_rate"],
                epochs=config["epochs"],
                batch_size=config["batch_size"],
                validation_data=None,  # No validation data provided for prediction
                validation_split=0.1,
                patience=5,
            )
            model = fine_tuner.fine_tune(layers_to_freeze=config["layers_to_freeze"])

        dataloader_input = DataLoader(
            matrix_input, batch_size=config["batch_size"], shuffle=False
        )
        # Prediction on provided data
        LOGGER.info("Starting prediction")
        pred_loss, pred_cor, pred_results, ground_truth = predict(
            model=model,
            dataloader_input=dataloader_input,
            loss_fn=loss_function,
            device=device,
            calibrate=args.calibrate,
            input_file=args.input,
            save_results=args.save,
        )
        LOGGER.info("Prediction completed.")
        # Generate Figures
        make_figures(
            predictions=pred_results,
            ground_truth=ground_truth,
            input_file=args.input,
            calibrated=args.calibrate,
            finetuned=args.finetune,
            save_results=args.save,
        )

    except Exception as e:
        LOGGER.error(f"An error occurred during execution: {e}")
        raise e
