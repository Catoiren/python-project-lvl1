"""Main even game module."""

import random

question_of_game = (
    'Answer "yes" if the number is even,'
    +
    ' otherwise answer "no".'
)


def is_even(num):
    """Check if num even or uneven.

    Args:
        num: int

    Returns:
        Return True or False.
    """
    return num != 0 and num % 2 == 0


def generate_round():
    """Ask question and give true answer.

    Returns:
        Return question and true answer.
    """
    max_number = 100
    num = random.randint(0, max_number)  # noqa: S311
    if is_even(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer
