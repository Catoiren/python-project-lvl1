"""Main gcd game module."""

import random

QUESTION_OF_GAME = (
    'Find the greatest common divisor of given numbers.'
)
MAX_NUMBER = 100


def find_common_divisor(first_num, second_num):
    """Find the greatest common divisor using Euclidean Algorithm.

    Args:
        first_num: int
        second_num: int

    Returns:
        Return greatest common divisor.
    """
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num
    return first_num + second_num


def generate_round():
    """Start gcd game round, find divisor.

    Returns:
        Return question and true answer.
    """
    operand1 = random.randint(0, MAX_NUMBER)  # noqa: S311
    operand2 = random.randint(0, MAX_NUMBER)  # noqa: S311
    question = '{0} {1}'.format(operand1, operand2)
    answer = find_common_divisor(operand1, operand2)
    return question, str(answer)
