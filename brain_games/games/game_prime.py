"""Main module for prime game."""

import random

QUESTION_OF_GAME = (
    'Answer "yes" if given number is prime, otherwise answer "no".'
)
MAX_NUMBER = 100


def is_prime(num):
    """Check if number is prime or not.

    Args:
        num: int

    Returns:
        Return bool.
    """
    if num <= 1:
        return False
    for counter in range(2, num - 1):
        if num % counter == 0:
            return False
        counter += 1
    return True


def generate_round():
    """Start prime game round.

    Returns:
        Return question and true answer.
    """
    num = random.randint(1, MAX_NUMBER)  # noqa: S311
    if is_prime(num):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return num, true_answer
