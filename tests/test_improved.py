from typing import Set, Tuple

from python.substring_finder_improved import SubstringFinderImproved
from tests.substring_tests import SubstringTests


class TestImproved(SubstringTests):
    def find_substrings(self, string_1: str, string_2: str, substring_length: int) -> Set[Tuple[int, int]]:
        return SubstringFinderImproved(string_1=string_1, string_2=string_2, substring_length=substring_length).find_substrings()
