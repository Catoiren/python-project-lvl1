"""Main calc game module."""

import operator
import random

question_of_game = (
    'What is the result of the expression?'
)


def generate_expression():
    """Generate expression.

    Returns:
        Returns two operands and operation.
    """
    max_number = 20
    return (random.randint(0, max_number),  # noqa: S311
            random.randint(0, max_number),  # noqa: S311
            random.choice(['+', '-', '*']),  # noqa: S311
            )


def generate_round():
    """Start calc game round, make calculation.

    Returns:
        Return question and true answer.
    """
    (operand1, operand2, operation) = generate_expression()
    question = '{a} {b} {c}'.format(a=operand1, b=operation, c=operand2)
    if operation == '+':
        answer = operator.add(operand1, operand2)
    elif operation == '-':
        answer = operator.sub(operand1, operand2)
    elif operation == '*':
        answer = operator.mul(operand1, operand2)
    return question, str(answer)
