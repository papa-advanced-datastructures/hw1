from python.naive import Naive


class TestNaive:
    def test_matching_strings(self):
        arbitrary_string = 'arbitrary'
        substrings = Naive(string_1=arbitrary_string, string_2=arbitrary_string, substring_length=len(arbitrary_string)).find_substrings()
        assert substrings == {(0, 0)}

    def test_second_string_is_shorter(self):
        string_1 = 'arbitrary'
        string_2 = 'arbitrar'
        substrings = Naive(string_1=string_1, string_2=string_2,
                           substring_length=len(string_2)).find_substrings()
        assert substrings == {(0, 0)}

    def test_first_string_is_shorter(self):
        string_1 = 'arbitrar'
        string_2 = 'arbitrary'
        substrings = Naive(string_1=string_1, string_2=string_2,
                           substring_length=len(string_1)).find_substrings()
        assert substrings == {(0, 0)}

    def test_substring_length_is_longer_than_first_word(self):
        string_1 = 'arbitrar'
        string_2 = 'arbitrary'
        substrings = Naive(string_1=string_1, string_2=string_2,
                           substring_length=len(string_2)).find_substrings()
        assert substrings == set()

    def test_substring_length_is_longer_than_second_word(self):
        string_1 = 'arbitrary'
        string_2 = 'arbitrar'
        substrings = Naive(string_1=string_1, string_2=string_2,
                           substring_length=len(string_1)).find_substrings()
        assert substrings == set()

    def test_no_substring_in_common(self):
        string_1 = 'abcd'
        string_2 = 'efgh'
        substrings = Naive(string_1=string_1, string_2=string_2,
                           substring_length=len(string_1)).find_substrings()
        assert substrings == set()

    def test_multiple_substrings_in_second_word(self):
        string_1 = 'abcd'
        string_2 = 'abcdefabcdef'
        substrings = Naive(string_1=string_1, string_2=string_2,
                           substring_length=2).find_substrings()
        assert substrings == {
            (0, 0),
            (0, 6),
            (1, 1),
            (1, 7),
            (2, 2),
            (2, 8),
        }
