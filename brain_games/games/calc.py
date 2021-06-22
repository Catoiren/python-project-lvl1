"""Main calc game module."""

import operator
import random

QUESTION_OF_GAME = (
    'What is the result of the expression?'
)
MAX_NUMBER = 20


def generate_answer(operand1, operand2):
    """Generate expression.

    Args:
        operand1: int
        operand2: int

    Returns:
        Return expression.
    """
    operations_dict = {operator.add: '+', operator.sub: '-', operator.mul: '*'}
    math_operator, operation_symbol = random.choice(  # noqa: S311
        list(operations_dict.items()),
    )
    return math_operator(operand1, operand2), operation_symbol


def generate_round():
    """Start calc game round, make calculation.

    Returns:
        Return question and true answer.
    """
    operand1 = random.randint(0, MAX_NUMBER)  # noqa: S311
    operand2 = random.randint(0, MAX_NUMBER)  # noqa: S311
    answer, symbol = generate_answer(operand1, operand2)
    question = '{0} {1} {2}'.format(operand1, symbol, operand2)
    return question, str(answer)
