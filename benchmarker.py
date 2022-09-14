import random
from dataclasses import dataclass
from datetime import datetime, timedelta
from functools import cached_property
from random import seed
from typing import List, Set, Tuple, Type

import numpy
from matplotlib import pyplot

from python.substring_finder import SubstringFinder
from python.substring_finder_improved import SubstringFinderImproved
from python.substring_finder_naive import SubstringFinderNaive
from tests.utilities import generate_random_string


@dataclass
class Solution:
    solution: Set[Tuple[int, int]]
    duration: timedelta
    hash_size: float


@dataclass
class ExperimentRun:
    naive: Solution
    complex: Solution

    def __str__(self):
        return f'Naive duration: {self.naive.duration}\nComplex duration: {self.complex.duration}'


class Experiment:
    def __init__(self, string1_length: int, string2_length: int, substring_length: int):
        self._string1_length = string1_length
        self._string2_length = string2_length
        self._substring_length = substring_length

    def run(self) -> ExperimentRun:
        return ExperimentRun(
            naive=self._find_solution(finder_type=SubstringFinderNaive),
            complex=self._find_solution(finder_type=SubstringFinderImproved)
        )

    def _find_solution(self, finder_type: Type[SubstringFinder]) -> Solution:
        finder = finder_type(string_1=self._string1, string_2=self._string2, substring_length=self._substring_length)

        start = datetime.now()
        solution = finder.find_substrings()
        end = datetime.now()

        return Solution(
            solution=solution,
            duration=end - start,
            hash_size=numpy.mean([len(finder._hash_of_first_string_substrings), len(finder._hash_of_second_string_substrings)])
        )

    @cached_property
    def _string1(self) -> str:
        return generate_random_string(number_of_characters=self._string1_length)

    @cached_property
    def _string2(self) -> str:
        return generate_random_string(number_of_characters=self._string2_length)


class BenchMarker:
    _NUMBER_OF_SEEDS = 5

    def __init__(self):
        self._string1_lengths = list(range(1, 1001))
        self._string2_lengths = list(range(1, 1001))

    def run(self):
        run_results = [self._get_single_run_random_string_random_substring_length(seed_number=seed_number)
                       for seed_number in range(self._NUMBER_OF_SEEDS)]
        self._plot_results(run_results)
        i = 0

    def _get_single_run_random_string_random_substring_length(self, seed_number: int) -> List[ExperimentRun]:
        seed(seed_number)
        string_pairs = zip(self._string1_lengths, self._string2_lengths)
        return [self._run_experiment(string1_length=string1_length,
                                     string2_length=string2_length,
                                     substring_length=random.randint(1, min(string1_length, string2_length)))
                for experiment_number, [string1_length, string2_length] in enumerate(string_pairs)]

    def _plot_results(self, run_results: List[List[ExperimentRun]]) -> None:
        naive_durations = numpy.mean(numpy.array([[result.naive.duration.microseconds for result in results]for results in run_results]), axis=0)
        complex_durations = numpy.mean(numpy.array([[result.complex.duration.microseconds for result in results] for results in run_results]), axis=0)

        number_of_experiments = list(range(len(run_results[0])))
        pyplot.plot(number_of_experiments, naive_durations, label='Naive')
        pyplot.plot(number_of_experiments, complex_durations, label='Rolling Hash')
        pyplot.legend()
        pyplot.title(f'Average Duration of Substring Finding methods\nAcross {self._NUMBER_OF_SEEDS} Random Substring Lengths')
        pyplot.xlabel('Initial string lengths')
        pyplot.ylabel('Microseconds')
        pyplot.show()

    def _run_experiment(self, string1_length: int, string2_length: int, substring_length: int) -> ExperimentRun:
        return Experiment(string1_length=string1_length, string2_length=string2_length, substring_length=substring_length).run()


if __name__ == '__main__':
    BenchMarker().run()
