"""Main calc game module."""

import operator
import random

QUESTION_OF_GAME = (
    'What is the result of the expression?'
)
MAX_NUMBER = 20


def generate_expression():
    """Generate expression.

    Returns:
        Returns two operands and operation.
    """
    return (random.randint(0, MAX_NUMBER),  # noqa: S311
            random.randint(0, MAX_NUMBER),  # noqa: S311
            random.choice(['+', '-', '*']),  # noqa: S311
            )


def generate_round():
    """Start calc game round, make calculation.

    Returns:
        Return question and true answer.
    """
    operand1, operand2, operation = generate_expression()
    question = '{0} {1} {2}'.format(operand1, operation, operand2)
    if operation == '+':
        answer = operator.add(operand1, operand2)
    elif operation == '-':
        answer = operator.sub(operand1, operand2)
    elif operation == '*':
        answer = operator.mul(operand1, operand2)
    else:
        return 'Unknown operation: {0}'.format(operation)
    return question, str(answer)
