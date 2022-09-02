from dataclasses import dataclass
from typing import Union


@dataclass
class Substring:
    starting_index: int
    hash_code: Union[str, int]


@dataclass
class PreviousHash:
    string: str
    value: int
