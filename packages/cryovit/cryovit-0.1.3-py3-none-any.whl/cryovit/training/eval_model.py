"""Script to evaluate segmentation models for CryoET data."""

import traceback
import warnings

import hydra

from cryovit._logging_config import setup_logging
from cryovit.config import BaseExperimentConfig, validate_experiment_config
from cryovit.run import eval_model

setup_logging("DEBUG")
import logging  # noqa: E402

warnings.simplefilter("ignore")


@hydra.main(
    config_path="../configs",
    config_name="eval_model.yaml",
    version_base="1.2",
)
def main(cfg: BaseExperimentConfig) -> None:
    """Main function to orchestrate the evaluation of segmentation models.

    First, it validates the configuration and, if valid, proceeds to run the evaluation process using
    the specified settings in the config file. It captures and logs any errors encountered during the
    evaluation process.

    Args:
        cfg (EvalModelConfig): Configuration object loaded from eval_model.yaml.
    """

    validate_experiment_config(cfg)

    try:
        eval_model.run_trainer(cfg)
    except BaseException as err:  # noqa: BLE001
        logging.error("%s: %s", type(err).__name__, err)
        logging.error(traceback.format_exc())


if __name__ == "__main__":
    main()
