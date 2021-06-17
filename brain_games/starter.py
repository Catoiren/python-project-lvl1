"""Main games module."""

import prompt

ROUNDS_COUNT = 3


def launch(game):
    """Launch games.

    Args:
        game: game module

    Returns:
        Return cli to player.
    """
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))
    print(game.QUESTION_OF_GAME)
    counter = 0
    while counter < ROUNDS_COUNT:
        question, true_answer = game.generate_round()
        print('Question: {0}'.format(question))
        player_answer = prompt.string(
            'Your answer: ',
        )
        if player_answer == true_answer:
            print('Correct!')
        else:
            print(
                ("'{0}' is wrong answer ;(. Correct answer was '{1}'."
                 ).format(player_answer, true_answer),
            )
            print("Let's try again, {0}!".format(player_name))
            return
        counter += 1
    print('Congratulations, {0}!'.format(player_name))
