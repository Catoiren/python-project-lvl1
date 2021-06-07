"""Main module for progression game."""

import random

question_of_game = (
    'What number is missing in the progression?'
)


def generate_progression(first_num, increaser, length_progression):
    """Generate math progression.

    Args:
        first_num: int
        increaser: int
        length_progression: int

    Returns:
        Return progression of 10 numbers.
    """
    progression = []
    index = 0
    while index <= length_progression:
        progression.append(str(first_num + increaser * index))
        index += 1
    return progression


def generate_round():
    """Start progression game round.

    Returns:
        Return question and true answer.
    """
    first_num = random.randint(1, 100)  # noqa: S311
    increaser = random.randint(2, 10)  # noqa: S311
    length_progression = 10
    progression = generate_progression(first_num, increaser, length_progression)
    missing_number = random.randint(0, length_progression)  # noqa: S311
    true_answer = progression.pop(missing_number)
    progression.insert(missing_number, '..')
    question = ' '.join(progression)
    return question, true_answer
