from random import choices
from string import ascii_letters, digits, punctuation


def generate_random_string(number_of_characters: int) -> str:
    return ''.join(choices(ascii_letters + digits + punctuation, k=number_of_characters))
