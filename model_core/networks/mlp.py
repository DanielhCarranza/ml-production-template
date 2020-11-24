"""Define mlp network function."""
from typing import Tuple


def mlp(
    input_shape: Tuple[int, ...],
    output_shape: Tuple[int, ...],
    layer_size: int = 128,
    dropout_amount: float = 0.2,
    num_layers: int = 3,
) -> ModelClass:
    """
    Simple MLP
    """
    return model
