import random
from dataclasses import dataclass
from datetime import datetime, timedelta
from random import seed
from typing import List, Set, Tuple, Type

import matplotlib as matplotlib
from matplotlib import pyplot

from python.substring_finder import SubstringFinder
from python.substring_finder_improved import SubstringFinderImproved
from python.substring_finder_naive import SubstringFinderNaive
from tests.utilities import generate_random_string


@dataclass
class Solution:
    solution: Set[Tuple[int, int]]
    duration: timedelta


@dataclass
class ExperimentRun:
    naive: Solution
    complex: Solution

    def __str__(self):
        return f'Naive duration: {self.naive.duration}\nComplex duration: {self.complex.duration}'


class Experiment:
    def __init__(self, string1_length: int, string2_length: int):
        self._string1_length = string1_length
        self._string2_length = string2_length

    def run(self) -> ExperimentRun:
        return ExperimentRun(
            naive=self._find_solution(finder_type=SubstringFinderNaive),
            complex=self._find_solution(finder_type=SubstringFinderImproved)
        )

    def _find_solution(self, finder_type: Type[SubstringFinder]) -> Solution:
        start = datetime.now()
        solution = finder_type(string_1=self._string1,
                               string_2=self._string2,
                               substring_length=self._substring_length).find_substrings()
        end = datetime.now()
        return Solution(
            solution=solution,
            duration=end - start
        )

    @property
    def _string1(self) -> str:
        return generate_random_string(number_of_characters=self._string1_length)

    @property
    def _string2(self) -> str:
        return generate_random_string(number_of_characters=self._string2_length)

    @property
    def _substring_length(self) -> int:
        return random.randint(1, min(self._string1_length, self._string2_length))


class BenchMarker:
    def __init__(self):
        seed(0)
        self._string1_lengths = list(range(1, 1001))
        self._string2_lengths = list(range(1, 1001))

    def run(self):
        string_pairs = zip(self._string1_lengths, self._string2_lengths)
        run_results = [self._run_experiment(string1_length, string2_length)
                       for experiment_number, [string1_length, string2_length] in enumerate(string_pairs)]
        self._plot_results(run_results)
        i = 0

    def _plot_results(self, run_results: List[ExperimentRun]) -> None:
        naive_durations = [results.naive.duration.microseconds for results in run_results]
        complex_durations = [results.complex.duration.microseconds for results in run_results]
        number_of_experiments = list(range(len(run_results)))
        pyplot.plot(number_of_experiments, naive_durations, label='Naive')
        pyplot.plot(number_of_experiments, complex_durations, label='Rolling Hash')
        pyplot.legend()
        pyplot.title('Duration of substring finding methods')
        pyplot.xlabel('Initial string lengths')
        pyplot.ylim('Microseconds')
        pyplot.show()

    def _run_experiment(self, string1_length: int, string2_length: int) -> ExperimentRun:
        return Experiment(string1_length=string1_length, string2_length=string2_length).run()


if __name__ == '__main__':
    BenchMarker().run()
