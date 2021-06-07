#!/usr/bin/env python3
"""Script to start progression game."""

from brain_games import starter
from brain_games.games import game_progression


def main():
    """Start game_progression."""
    starter.start(game_progression)


if __name__ == '__main__':
    main()
