"""Main module for prime game."""

import random

QUESTION_OF_GAME = (
    'Answer "yes" if given number is prime, otherwise answer "no".'
)


def is_prime(num):
    """Check if number is prime or not.

    Args:
        num: int

    Returns:
        Return bool.
    """
    if num == 1:
        return False
    index = 2
    while index < num:
        if num % index == 0:
            return False
        index += 1
    return True


def generate_round():
    """Start prime game round.

    Returns:
        Return question and true answer.
    """
    num = random.randint(1, 100)  # noqa: S311
    if is_prime(num) is True:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return num, true_answer
