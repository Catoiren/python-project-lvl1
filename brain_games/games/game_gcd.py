"""Main gcd game module."""

import random

question_of_game = (
    'Find the greatest common divisor of given numbers.'
)


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
    max_number = 100
    operand1 = random.randint(0, max_number)  # noqa: S311
    operand2 = random.randint(0, max_number)  # noqa: S311
    question = '{a} {b}'.format(a=operand1, b=operand2)
    answer = find_common_divisor(operand1, operand2)
    return question, str(answer)
