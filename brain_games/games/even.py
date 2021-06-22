"""Main even game module."""

import random

QUESTION_OF_GAME = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)
MAX_NUMBER = 100


def is_even(num):
    """Check if num even or uneven.

    Args:
        num: int

    Returns:
        Return True or False.
    """
    return num % 2 == 0


def generate_round():
    """Ask question and give true answer.

    Returns:
        Return question and true answer.
    """
    num = random.randint(0, MAX_NUMBER)  # noqa: S311
    if is_even(num):
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer
