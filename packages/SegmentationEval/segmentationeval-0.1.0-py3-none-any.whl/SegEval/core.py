import numpy as np
from PIL import Image


class SegEval:
    """
    A class to calculate common segmentation evaluation metrics.

    Args:
        ground_truth (np.ndarray): The ground truth segmentation mask.
                                   Non-zero values are considered positive.
        segresult (np.ndarray): The predicted segmentation mask.
                                Non-zero values are considered positive.
    """

    def __init__(self, ground_truth, segresult):
        # Ensure images have the same shape
        if ground_truth.shape != segresult.shape:
            raise ValueError("Images must have the same shape.")

        # Convert arrays to boolean type for consistent logic
        # True represents the positive class (foreground)
        # False represents the negative class (background)
        self.ground_truth = ground_truth.astype(bool)
        self.segresult = segresult.astype(bool)

        # Initialize metric attributes to None
        self.tp = None
        self.fn = None
        self.fp = None
        self.tn = None

        # Calculate all stats upon initialization
        self._calculate_stats()

    def _calculate_stats(self):
        """Calculates TP, FN, FP, TN and stores them as attributes."""
        # True Positive (TP): correctly identified positive pixels
        self.tp = np.sum(np.logical_and(self.ground_truth, self.segresult))

        # False Negative (FN): positive pixels that were missed
        self.fn = np.sum(np.logical_and(self.ground_truth, np.logical_not(self.segresult)))

        # False Positive (FP): negative pixels that were wrongly identified as positive
        self.fp = np.sum(np.logical_and(np.logical_not(self.ground_truth), self.segresult))

        # True Negative (TN): correctly identified negative pixels
        self.tn = np.sum(np.logical_and(np.logical_not(self.ground_truth), np.logical_not(self.segresult)))

    def get_stats(self):
        """Returns a dictionary of the basic confusion matrix elements."""
        return {
            "TP": self.tp,
            "FN": self.fn,
            "FP": self.fp,
            "TN": self.tn
        }

    def IoU(self):
        """
        Calculates Intersection over Union (IoU), also known as the Jaccard index.
        Formula: TP / (TP + FP + FN)
        """
        denominator = self.tp + self.fp + self.fn
        if denominator == 0:
            return float('nan')  # Return NaN if denominator is zero
        return self.tp / denominator

    def Precision(self):
        """
        Calculates the precision.
        Formula: TP / (TP + FP)
        """
        denominator = self.tp + self.fp
        if denominator == 0:
            return float('nan')
        return self.tp / denominator

    def Recall(self):
        """
        Calculates the recall (Sensitivity or True Positive Rate).
        Formula: TP / (TP + FN)
        """
        denominator = self.tp + self.fn
        if denominator == 0:
            return float('nan')
        return self.tp / denominator

    def F1_score(self):
        """
        Calculates the F1 score.
        Formula: 2 * (Precision * Recall) / (Precision + Recall)
        """
        precision = self.Precision()
        recall = self.Recall()
        if np.isnan(precision) or np.isnan(recall) or (precision + recall) == 0:
            return float('nan')
        return 2 * (precision * recall) / (precision + recall)

    def Accuracy(self):
        """
        Calculates the accuracy.
        Formula: (TP + TN) / (Total Pixels)
        """
        total_pixels = self.tp + self.tn + self.fp + self.fn
        if total_pixels == 0:
            return float('nan')
        return (self.tp + self.tn) / total_pixels