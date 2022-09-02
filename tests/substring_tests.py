from abc import ABC, abstractmethod
from typing import Set, Tuple


class SubstringTests(ABC):
    @abstractmethod
    def find_substrings(self, string_1: str, string_2: str, substring_length: int) -> Set[Tuple[int, int]]:
        pass

    def test_matching_strings(self):
        arbitrary_string = 'arbitrary'
        substrings = self.find_substrings(string_1=arbitrary_string, string_2=arbitrary_string, substring_length=len(arbitrary_string))
        assert substrings == {(0, 0)}

    def test_second_string_is_shorter(self):
        string_1 = 'arbitrary'
        string_2 = 'arbitrar'
        substrings = self.find_substrings(string_1=string_1, string_2=string_2, substring_length=len(string_2))
        assert substrings == {(0, 0)}

    def test_first_string_is_shorter(self):
        string_1 = 'arbitrar'
        string_2 = 'arbitrary'
        substrings = self.find_substrings(string_1=string_1, string_2=string_2, substring_length=len(string_1))
        assert substrings == {(0, 0)}

    def test_substring_length_is_longer_than_first_word(self):
        string_1 = 'arbitrar'
        string_2 = 'arbitrary'
        substrings = self.find_substrings(string_1=string_1, string_2=string_2, substring_length=len(string_2))
        assert substrings == set()

    def test_substring_length_is_longer_than_second_word(self):
        string_1 = 'arbitrary'
        string_2 = 'arbitrar'
        substrings = self.find_substrings(string_1=string_1, string_2=string_2, substring_length=len(string_1))
        assert substrings == set()

    def test_no_substring_in_common(self):
        string_1 = 'abcd'
        string_2 = 'efgh'
        substrings = self.find_substrings(string_1=string_1, string_2=string_2, substring_length=len(string_1))
        assert substrings == set()

    def test_multiple_substrings_in_second_word(self):
        string_1 = 'abcd'
        string_2 = 'abcdefabcdef'
        substrings = self.find_substrings(string_1=string_1, string_2=string_2, substring_length=2)
        assert substrings == {
            (0, 0),
            (0, 6),
            (1, 1),
            (1, 7),
            (2, 2),
            (2, 8),
        }
