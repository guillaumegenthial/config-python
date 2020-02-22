"""Config file using python"""

from libnn.vocab import Vocab
from libnn.layers import TimesTwoLayer, PlusOneLayer
from libnn.model import Model


vocab = Vocab(["foo", "bar"])
layers = [
    TimesTwoLayer("times_two", vocab),
    PlusOneLayer("plus_one", vocab),
]
model = Model(layers)
