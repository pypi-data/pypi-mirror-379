"""Metrics for evaluating CryoVIT segmentation models."""

import torch
from torch import Tensor
from torchmetrics import Metric


class DiceMetric(Metric):
    """Metric class for calculating the Dice score to evaluate segmentation models."""

    higher_is_better = True

    def __init__(self, threshold: float, **kwargs):
        """Initializes the DiceMetric instance with a threshold for binary classification.

        Args:
            threshold (float): The threshold to apply to the predictions during Dice score calculation.
        """

        super().__init__()
        self.name = "DiceMetric"
        self.thresh = threshold
        self.add_state(
            "dice_score", default=torch.tensor(0.0), dist_reduce_fx="sum"
        )
        self.add_state(
            "total", default=torch.tensor(0.0), dist_reduce_fx="sum"
        )

    def update(self, y_pred: Tensor, y_true: Tensor) -> None:
        """Updates the states for the Dice score computation based on predictions and actual values.

        Args:
            y_pred (Tensor): Predicted probabilities or logits from the model.
            y_true (Tensor): Ground truth labels.
        """

        y_pred = torch.where(y_pred < self.thresh, 0.0, 1.0)

        intersection = torch.sum(y_true * y_pred)
        denom = torch.sum(y_true) + torch.sum(y_pred)

        self.dice_score += 2 * intersection / (denom + 1e-3)
        self.total += 1

    def compute(self) -> Tensor:
        """Computes the final Dice score over all updates.

        Returns:
            Tensor: The average Dice score across all batches.
        """

        return self.dice_score / self.total if self.total > 0 else torch.tensor(0.0)  # type: ignore


class F1Metric(Metric):
    """Metric class for calculating the F1 score to evaluate segmentation models."""

    def __init__(self, **kwargs):
        """Initializes the F1Metric instance."""

        super().__init__()
        self.name = "F1Metric"
        self.add_state("f1", default=torch.tensor(0.0), dist_reduce_fx="sum")
        self.add_state(
            "total", default=torch.tensor(0.0), dist_reduce_fx="sum"
        )

    def update(self, y_pred: Tensor, y_true: Tensor) -> None:
        """Updates the states for the F1 score computation based on predictions and actual values.

        Args:
            y_pred (Tensor): Predicted probabilities or logits from the model.
            y_true (Tensor): Ground truth labels.
        """
        y_pred = (y_pred > 0.5).float()
        tp = torch.sum(y_true * y_pred)
        fp = torch.sum((1 - y_true) * y_pred)
        fn = torch.sum(y_true * (1 - y_pred))
        precision = tp / (tp + fp + 1e-6)
        recall = tp / (tp + fn + 1e-6)
        f1 = 2 * (precision * recall) / (precision + recall + 1e-6)
        self.f1 += f1
        self.total += 1

    def compute(self) -> Tensor:
        """Computes the final F1 score over all updates.

        Returns:
            Tensor: The average F1 score across all batches.
        """

        return self.f1 / self.total if self.total > 0 else torch.tensor(0.0)  # type: ignore
