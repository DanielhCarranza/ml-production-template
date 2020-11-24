"""Predictor class"""
from typing import Tuple, Union

import numpy as np

from model_core.models import SomeModel
from model_core.datasets import ImageDataset, TextDataset, SomeDataset
import model_core.util as util


class Predictor:
    """Wrap the model and predict something """

    def __init__(self, dataset_cls=SomeDataset):
        self.model = SomeModel(dataset_cls=dataset_cls)
        self.model.load_weights()

    def predict(self, something_or_filename: Union[np.ndarray, str]) -> Tuple[str, float]:
        """Predict  something"""
        if isinstance(something_or_filename, str):
            obj = util.read_something(something_or_filename)
        else:
            obj = something_or_filename
        return self.model.predict(obj)

    def evaluate(self, dataset):
        """Evaluate on a dataset."""
        return self.model.evaluate(dataset.x_test, dataset.y_test)
