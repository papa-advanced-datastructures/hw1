from typing import Iterable, Optional

from python.definitions import PreviousHash, Substring
from python.rolling_hash import RollingHash
from python.substring_finder import SubstringFinder


class SubstringFinderImproved(SubstringFinder):
    def _get_all_substring_hashes(self, full_string: str) -> Iterable[Substring]:
        initial_substring = full_string[:self._substring_length]
        substring = self._get_substring(string=initial_substring, starting_index=0, previous_hash=None)
        yield substring
        previous_hash = PreviousHash(
            string=initial_substring,
            value=substring.hash_code
        )
        for next_starting_index in range(len(full_string) - self._substring_length):
            next_character = full_string[next_starting_index + self._substring_length]
            substring = self._get_substring(string=next_character, starting_index=next_starting_index, previous_hash=previous_hash)
            yield substring
            previous_hash = PreviousHash(
                string=next_character,
                value=substring.hash_code
            )

    def _get_substring(self, string: str, starting_index: int, previous_hash: Optional[PreviousHash]) -> Substring:
        return Substring(
                starting_index=starting_index,
                hash_code=RollingHash(string=string, previous_hash=previous_hash).run(),
            )
