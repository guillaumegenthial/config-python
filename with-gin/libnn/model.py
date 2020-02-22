"""Base Class for Models"""

from typing import List

import gin

from libnn.layers import BaseLayer


@gin.configurable
class Model:
    """Base Class for Models"""

    def __init__(self, layers: List[BaseLayer]):
        self.layers = layers

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.layers})"

    def forward(self, x: int) -> int:
        for layer in self.layers:
            x = layer.forward(x)
        return x
