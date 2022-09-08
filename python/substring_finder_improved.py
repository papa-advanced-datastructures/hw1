from typing import Iterable

from python.definitions import PreviousHash, Substring
from python.rolling_hash import RollingHash
from python.substring_finder import SubstringFinder


class SubstringFinderImproved(SubstringFinder):
    def __init__(self, string_1: str, string_2: str, substring_length: int, salt: int = 100):
        super().__init__(string_1=string_1, string_2=string_2, substring_length=substring_length)
        self._salt = salt

    def _get_all_substring_hashes(self, full_string: str) -> Iterable[Substring]:
        previous_substring = Substring(
            starting_index=0,
            hash_code=RollingHash(string_to_add=full_string[:self._substring_length], salt=self._salt).run()
        )
        yield previous_substring
        for next_character in full_string[self._substring_length:]:
            previous_hash = PreviousHash(
                first_character=full_string[previous_substring.starting_index],
                value=previous_substring.hash_code,
                window_size=self._substring_length
            )
            previous_substring = Substring(
                starting_index=previous_substring.starting_index + 1,
                hash_code=RollingHash(string_to_add=next_character, previous_hash=previous_hash, salt=self._salt).run()
            )
            yield previous_substring
