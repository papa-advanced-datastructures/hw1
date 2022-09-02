from typing import Iterable

from python.definitions import Substring
from python.substring_finder import SubstringFinder


class SubstringFinderNaive(SubstringFinder):
    def _get_all_substring_hashes(self, full_string: str) -> Iterable[Substring]:
        for start_index in range(len(full_string[:-self._substring_length]) + 1):
            substring = full_string[start_index:start_index + self._substring_length]
            yield Substring(
                starting_index=start_index,
                hash_code=substring,
            )
