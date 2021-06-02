"""Main games module."""
import prompt


def start(game):
    """Start games.

    Args:
        game: str

    Returns:
        Return cli to player.
    """
    print('Welcome to the Brain Games!')  # noqa: WPS421
    player_name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=player_name))  # noqa: WPS421
    print(game.question_of_game)  # noqa: WPS421
    index = 0
    while index < 3:
        (question, true_answer) = (game.generate_round())
        player_answer = prompt.string(
            'Question: {a}\nYour answer: '.format(a=question),
        )
        if player_answer == true_answer:
            print('Correct!')  # noqa: WPS421
        else:
            print(  # noqa: WPS421
                ("'{a}' is wrong answer ;(. Correct answer was '{b}'."
                 ).format(a=player_answer, b=true_answer),
            )
            return print(  # noqa: WPS421
                "Let's try again, {a}!".format(a=player_name),
            )
        index += 1
    return print(  # noqa: WPS421
        'Congratulations, {a}!'.format(a=player_name),
    )
