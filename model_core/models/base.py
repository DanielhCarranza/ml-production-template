"""Model class, to be extended by specific types of models."""
from pathlib import Path
from typing import Callable, Dict, Optional

import numpy as np



DIRNAME = Path(__file__).parents[1].resolve() / "weights"


class Model:
    """Base class, to be subclassed by predictors for specific type of data."""

    def __init__(
        self,
        dataset_cls: type,
        network_fn: Callable,
        dataset_args: Dict = None,
        network_args: Dict = None,
    ):
        self.name = f"{self.__class__.__name__}_{dataset_cls.__name__}_{network_fn.__name__}"

        if dataset_args is None:
            dataset_args = {}
        self.data = dataset_cls(**dataset_args)

        if network_args is None:
            network_args = {}
        self.network = network_fn(**network_args)
        self.network.summary()

        self.batch_augment_fn: Optional[Callable] = None
        self.batch_format_fn: Optional[Callable] = None

    @property
    def weights_filename(self) -> str:
        DIRNAME.mkdir(parents=True, exist_ok=True)
        return str(DIRNAME / f"{self.name}_weights.h5")

    def fit(
        self, dataset, batch_size: int = 32, epochs: int = 10, augment_val: bool = True, callbacks: list = None,
    ):
        pass

    def evaluate(self, x: np.ndarray, y: np.ndarray, batch_size: int = 16, _verbose: bool = False):
        pass

    def loss(self): 
        return "categorical_crossentropy"

    def optimizer(self):  
        return "Adam()"

    def metrics(self):  
        return ["accuracy"]

    def load_weights(self):
        self.network.load_weights(self.weights_filename)

    def save_weights(self):
        self.network.save_weights(self.weights_filename)
