"""Vocabulary"""

from typing import List


class Vocab:
    """Vocabulary"""

    def __init__(self, words: List[str]):
        self.words = words

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.words}, id={id(self)})"
