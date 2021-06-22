#!/usr/bin/env python3
"""Script to start progression game."""

from brain_games import starter
from brain_games.games import progression


def main():
    """Launch game_progression."""
    starter.launch(progression)


if __name__ == '__main__':
    main()
