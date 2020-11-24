"""Model class, to be extended by specific types of models."""
import os
import pickle
from pathlib import Path
from typing import Callable, Dict, Optional, Union, List, Tuple

import numpy as np

import torch
import torch.nn as nn


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
        raise NotImplementedError

    def evaluate(self, x: np.ndarray, y: np.ndarray, batch_size: int = 16, _verbose: bool = False):
        raise NotImplementedError

    def loss(self): 
        pass 

    def optimizer(self):  
        pass 

    def metrics(self):  
        pass 

    def load_weights(self):
        self.network.load_weights(self.weights_filename)

    def save_weights(self):
        self.network.save_weights(self.weights_filename)


class TorchModelBase(Model):
    def __init__(self,
            dataset_cls: type,
            network_fn: Callable,
            dataset_args: Dict = None,
            network_args: Dict = None,
            optimizer_cls:Callable=torch.optim.Adam,
            optimizer_args:Dict=None,
            device=None,
            ):
        super().__init__(dataset_cls, network_fn, dataset_args, network_args)

        if optimizer_args is None: 
            self.optimizer_args = {}
        else: 
            self.optimizer_args=optimizer_args
        self.optimizer_cls = optimizer_cls

        if device is None:
            self.device = torch.device( "cuda" if torch.cuda.is_available() else "cpu" )

    def optimizer_fn(self):
        return self.optimizer_cls(self.model.parameters(), **self.optimizer_args)
            
    def loss_fn(self, **loss_args):
        return nn.CrossEntropyLoss(**loss_args)

    def metrics(self, preds, yb):
        acc  = (preds.argmax(-1)==yb).float()
        return acc

    def fit(self, *args):
        self.model=self.network().to(self.device)
        self.optimizer = self.optimizer_fn()
        self.loss = self.loss_fn()
        self.model.train()
        self.acc, self.error = [], []
        for i, (xb, yb) in enumerate(self.data):
            preds = self.model(xb)
            self.loss(preds, yb)
            self.loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()
            self.acc.append(self.metrics(preds, yb))
            self.error.append(self.loss.item())
        return self


    def evaluate(self, xb, yb, device:str=None):
        device = self.device if device is None else torch.device(device)

        self.model.to(device)
        self.model.eval()
        with torch.no_grad():
            for i, (xb, yb) in enumerate(self.data):
                preds = self.model(xb)
                self.loss(preds, yb)
                self.metrics(preds, yb)
        return self

    def to_pickle(self, output_filename:str):
        """
        Serialize the entire class instance
        """
        self.model = self.model.cpu()
        with open(output_filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle(src_filename:str):
        """
        Load an entire class instance onto the CPU.
        """
        with open(src_filename, 'rb') as f:
            return pickle.load(f)
