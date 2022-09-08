from typing import Optional

import numpy as numpy

from python.definitions import PreviousHash


class RollingHash:
    def __init__(self, string_to_add: str, previous_hash: Optional[PreviousHash] = None, salt: int = 100):
        self._previous_hash = previous_hash
        self._salt = salt
        self._string_to_add = string_to_add

    def run(self) -> int:
        return self._hash_without_previous() if self._previous_hash is None else self._hash_with_previous()

    def _hash_without_previous(self):
        characters_binary_value = [self._get_character_binary_value(character=character) for character in self._string_to_add]
        multiplication_values = numpy.array([self._salt ** (exponent - 1) for exponent in range(len(self._string_to_add), 0, -1)])
        encoded_characters = numpy.prod(numpy.array([characters_binary_value, multiplication_values]), axis=0)
        return sum(encoded_characters)

    def _hash_with_previous(self):
        unwanted_character = self._previous_hash.first_character
        previous_first_character_binary_value = self._get_character_binary_value(character=unwanted_character)
        previous_first_character_encoded_value = previous_first_character_binary_value * self._salt ** (self._previous_hash.window_size - 1)
        base_value = self._previous_hash.value - previous_first_character_encoded_value
        return base_value * self._salt + self._get_character_binary_value(character=self._string_to_add)

    def _get_character_binary_value(self, character: str) -> int:
        return numpy.mod(ord(character), self._salt - 1) + 1
