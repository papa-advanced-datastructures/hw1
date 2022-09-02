from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Set, Tuple


class SubstringFinder(ABC):
    def __init__(self, string_1: str, string_2: str, substring_length: int):
        self._string_1 = string_1
        self._string_2 = string_2
        self._substring_length = substring_length
        self._hash = defaultdict(set)

    @abstractmethod
    def find_substrings(self) -> Set[Tuple[int, int]]:
        pass
