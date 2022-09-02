from _pytest.fixtures import fixture

from python.substring_finder_improved import SubstringFinderImproved
from python.substring_finder_naive import SubstringFinderNaive
from tests.utilities import generate_random_string


class TestLargeStrings:
    _number_of_characters = 10000
    _substring_length = 107

    @fixture(autouse=True)
    def _set_random_strings(self):
        self._string_1 = generate_random_string(number_of_characters=self._number_of_characters)
        self._string_2 = generate_random_string(number_of_characters=self._number_of_characters)

    def test_large_strings(self):
        substrings_naive = SubstringFinderNaive(string_1=self._string_1, string_2=self._string_2, substring_length=self._substring_length).find_substrings()
        substrings_improved = SubstringFinderImproved(string_1=self._string_1, string_2=self._string_2, substring_length=self._substring_length).find_substrings()
        assert substrings_naive == substrings_improved

    def test_naive_performance(self):
        SubstringFinderNaive(string_1=self._string_1, string_2=self._string_2, substring_length=self._substring_length).find_substrings()

    def test_improved_performance(self):
        SubstringFinderImproved(string_1=self._string_1, string_2=self._string_2, substring_length=self._substring_length).find_substrings()
