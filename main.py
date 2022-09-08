import sys
from typing import Set, Tuple

from python.substring_finder_improved import SubstringFinderImproved


class Main:
    def __init__(self, args):
        self._string_1_filename = args[1]
        self._string_2_filename = args[2]
        self._substring_length = int(args[3])

    def run(self) -> Set[Tuple[int, int]]:
        return SubstringFinderImproved(string_1=self._string_1, string_2=self._string_2, substring_length=self._substring_length).find_substrings()

    @property
    def _string_1(self) -> str:
        return self._read_file(filename=self._string_1_filename)

    @property
    def _string_2(self) -> str:
        return self._read_file(filename=self._string_2_filename)

    def _read_file(self, filename: str) -> str:
        with open(filename, 'r') as f:
            return f.read()


if __name__ == '__main__':
    print(Main(sys.argv).run())
