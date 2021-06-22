"""Main module for progression game."""

import random

QUESTION_OF_GAME = (
    'What number is missing in the progression?'
)
MAX_FIRST_NUMBER = 100
MIN_PROGRESSION_DIFF = 2
MAX_PROGRESSION_DIFF = 10
PROGRESSION_LENGTH = 10


def generate_progression(first_num, progression_diff):
    """Generate math progression.

    Args:
        first_num: int
        progression_diff: int

    Returns:
        Return progression of 10 numbers.
    """
    progression = []
    for index in range(PROGRESSION_LENGTH):
        progression.append(str(first_num + progression_diff * index))
    return progression


def generate_round():
    """Start progression game round.

    Returns:
        Return question and true answer.
    """
    first_num = random.randint(1, MAX_FIRST_NUMBER)  # noqa: S311
    progression_diff = random.randint(  # noqa: S311
        MIN_PROGRESSION_DIFF, MAX_PROGRESSION_DIFF,
    )
    progression = generate_progression(first_num, progression_diff)
    missing_number_index = random.randint(0, len(progression))  # noqa: S311
    true_answer = progression[missing_number_index]
    progression[missing_number_index] = '..'
    return ' '.join(progression), true_answer
