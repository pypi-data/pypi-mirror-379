import logging
from pathlib import Path
from typing import Any

import h5py
import numpy as np
import pandas as pd
from pytorch_lightning import Callback, LightningModule, Trainer
from pytorch_lightning.callbacks.prediction_writer import BasePredictionWriter
from pytorch_lightning.utilities.types import STEP_OUTPUT

from cryovit.types import BatchedModelResult


class TestPredictionWriter(Callback):
    """Callback to write predictions to disk during model evaluation."""

    def __init__(self, results_dir: Path, label_key: str, **kwargs) -> None:
        """Creates a callback to save predictions on the test data.

        Args:
            results_dir (Path): directory in which the predictions should be saved.
        """

        self.results_dir = (
            results_dir if isinstance(results_dir, Path) else Path(results_dir)
        )
        self.label_key = label_key

    def on_test_batch_end(
        self,
        trainer: Trainer,
        pl_module: LightningModule,
        outputs: STEP_OUTPUT,
        batch: Any,
        batch_idx: int,
        dataloader_idx: int = 0,
    ) -> None:
        """Handles the end of a test batch to save outputs."""

        assert isinstance(outputs, BatchedModelResult)
        for n in range(outputs.num_tomos):
            output_file = (
                self.results_dir / outputs.samples[n] / outputs.tomo_names[n]
            )
            output_file.parent.mkdir(parents=True, exist_ok=True)

            # Binary classify predictions into segmentations and convert to correct formats
            data = outputs.data[n]
            labels = outputs.label[n]
            preds = outputs.preds[n]

            with h5py.File(output_file, "w") as fh:
                fh.create_dataset(
                    "data", data=data, shape=data.shape, dtype=data.dtype
                )
                fh.create_dataset(self.label_key, data=labels, shape=labels.shape, dtype=labels.dtype, compression="gzip")  # type: ignore
                fh.create_dataset(f"{self.label_key}_preds", data=preds, shape=preds.shape, dtype=preds.dtype, compression="gzip")  # type: ignore

                if outputs.aux_data is not None:
                    fh.create_group("aux_data")
                    for key in outputs.aux_data:
                        fh["aux_data"].create_dataset(key, data=outputs.aux_data[key], compression="gzip")  # type: ignore


class PredictionWriter(BasePredictionWriter):
    """Callback to write predictions to disk during model prediction."""

    def __init__(
        self, results_dir: Path, label_key: str, threshold: float, **kwargs
    ) -> None:
        """Creates a callback to save predictions on the test data.

        Args:
            results_dir (Path): directory in which the predictions should be saved.
        """

        super().__init__(write_interval="batch", **kwargs)
        self.results_dir = (
            results_dir if isinstance(results_dir, Path) else Path(results_dir)
        )
        self.label_key = label_key
        self.threshold = threshold
        self.result_paths = []

    def write_on_batch_end(
        self,
        trainer: Trainer,
        pl_module: LightningModule,
        prediction: BatchedModelResult,
        batch_indices,
        batch: Any,
        batch_idx: int,
        dataloader_idx: int,
    ) -> None:
        """Handles the end of a prediction batch to save outputs."""

        for n in range(prediction.num_tomos):
            result_path = self.results_dir / prediction.tomo_names[n]
            result_path = result_path.with_suffix(".hdf")
            result_path.parent.mkdir(parents=True, exist_ok=True)
            # Binary classify predictions into segmentations and convert to correct formats
            data = prediction.data[n].astype(np.float32)
            preds = prediction.preds[n]
            segs = (preds >= self.threshold).astype(
                np.uint8
            )  # Binary segmentation
            # Save data and pred to HDF5
            with h5py.File(result_path, "w") as fh:
                fh.create_dataset("data", data=data, compression="gzip")
                fh.create_dataset(
                    f"{self.label_key}_preds", data=segs, compression="gzip"
                )
            self.result_paths.append(result_path)


class CsvWriter(Callback):
    """Callback to save model performance metrics to a .csv."""

    def __init__(self, csv_result_path: Path, **kwargs) -> None:
        """Creates a callback to save performance metrics on the test data.

        Args:
            csv_result_path (Path): .csv file in which metrics should be saved.
        """

        self.csv_result_path = (
            csv_result_path
            if isinstance(csv_result_path, Path)
            else Path(csv_result_path)
        )
        self.csv_result_path.parent.mkdir(parents=True, exist_ok=True)

    def _create_metric_df(
        self,
        sample: str,
        tomo_name: str,
        split_id: int | None = None,
        **metrics,
    ) -> pd.DataFrame:
        result_dict: dict[str, Any] = {
            "sample": sample,
            "tomo_name": tomo_name,
        }
        for name, value in metrics.items():
            result_dict[name] = [value]
        if split_id is not None:
            result_dict["split_id"] = [split_id]

        return pd.DataFrame(result_dict)

    def on_test_batch_end(
        self,
        trainer: Trainer,
        pl_module: LightningModule,
        outputs: STEP_OUTPUT,
        batch: Any,
        batch_idx: int,
        dataloader_idx: int = 0,
    ) -> None:
        """Handles the end of a test batch to save metrics."""

        assert isinstance(outputs, BatchedModelResult)
        assert (
            outputs.num_tomos == 1
        ), "TestPredictionWriter only supports single-tomogram batches."
        sample, tomo_name, split_id = (
            outputs.samples[0],
            outputs.tomo_names[0],
            outputs.split_id[0] if outputs.split_id is not None else None,
        )

        # Create results .csv if it doesn't exist
        metric_names = list(outputs.metrics)
        column_names = ["sample", "tomo_name"] + metric_names
        if split_id is not None:
            column_names += ["split_id"]
        if not self.csv_result_path.exists():
            results_df = pd.DataFrame(columns=column_names)
        else:
            results_df = pd.read_csv(self.csv_result_path)

        # Warn if row already exists and remove (i.e., replace)
        matching_rows = (results_df["tomo_name"] == tomo_name) & (
            results_df["sample"] == sample
        )
        if split_id is not None and "split_id" in results_df.columns:
            matching_rows = matching_rows & (
                results_df["split_id"] == split_id
            )
        if matching_rows.any():
            logging.warning(
                "Data with sample %s, name %s, and split %s already has an entry. Replacing %d rows...",
                sample,
                tomo_name,
                split_id,
                matching_rows.sum(),
            )
            results_df = results_df[~matching_rows]
        # Add metrics to df
        metrics_df = self._create_metric_df(
            sample, tomo_name, split_id, **outputs.metrics
        )
        if results_df.empty:
            results_df = metrics_df
        else:
            results_df = pd.concat([results_df, metrics_df], ignore_index=True)
        results_df.to_csv(self.csv_result_path, mode="w", index=False)
