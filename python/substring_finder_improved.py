from typing import Iterable

from python.definitions import PreviousHash, Substring
from python.rolling_hash import RollingHash
from python.substring_finder import SubstringFinder


class SubstringFinderImproved(SubstringFinder):
    def _get_all_substring_hashes(self, full_string: str) -> Iterable[Substring]:
        previous_hash = None
        for start_index in range(len(full_string[:-self._substring_length]) + 1):
            substring = full_string[start_index:start_index + self._substring_length]
            previous_hash = RollingHash(string=substring, previous_hash=previous_hash).run()
            yield Substring(
                starting_index=start_index,
                hash_code=previous_hash,
            )
            previous_hash = PreviousHash(
                string=substring,
                value=previous_hash
            )
