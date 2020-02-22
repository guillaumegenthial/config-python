"""Layer Classes"""

from abc import ABC, abstractmethod

from libnn.vocab import Vocab


class BaseLayer(ABC):
    """Interface for Layers

    Attributes
    ----------
    name : str
        Name of the layer
    vocab : Vocab
        Vocabulary, illustrates the need for complex dependencies
    """

    def __init__(self, name: str, vocab: Vocab):
        self.name = name
        self.vocab = vocab

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.vocab})"

    @abstractmethod
    def forward(self, x: int) -> int:
        raise NotImplementedError


class TimesTwoLayer(BaseLayer):

    def forward(self, x: int) -> int:
        return 2 * x


class PlusOneLayer(BaseLayer):

    def forward(self, x: int) -> int:
        return x + 1
