import itertools
from collections import defaultdict
from functools import cached_property
from typing import Dict, Iterable, Set, Tuple

from python.definitions import Substring


class Naive:
    def __init__(self, string_1: str, string_2: str, substring_length: int):
        self._string_1 = string_1
        self._string_2 = string_2
        self._substring_length = substring_length
        self._hash = defaultdict(set)

    def find_substrings(self) -> Set[Tuple[int, int]]:
        starting_index_pairs = set()
        for substring, first_string_starting_indices in self._hash_of_first_string_substrings.items():
            second_string_starting_indices = self._hash_of_second_string_substrings.get(substring, None)
            if second_string_starting_indices:
                substring_index_pairs = itertools.product(first_string_starting_indices, second_string_starting_indices)
                starting_index_pairs.update(set(substring_index_pairs))
        return starting_index_pairs

    @cached_property
    def _hash_of_first_string_substrings(self) -> Dict[str, Set[int]]:
        return self._hash_substrings(full_string=self._string_1)

    @cached_property
    def _hash_of_second_string_substrings(self) -> Dict[str, Set[int]]:
        return self._hash_substrings(full_string=self._string_2)

    def _hash_substrings(self, full_string: str) -> Dict[str, Set[int]]:
        substring_hash = defaultdict(set)
        for first_string_substring in self._get_all_substrings(full_string=full_string):
            substring_hash[first_string_substring.substring].add(first_string_substring.starting_index)
        return substring_hash

    def _get_all_substrings(self, full_string: str) -> Iterable[Substring]:
        for start_index in range(len(full_string[:-self._substring_length]) + 1):
            substring = full_string[start_index:start_index + self._substring_length]
            yield Substring(
                starting_index=start_index,
                substring=substring,
            )
