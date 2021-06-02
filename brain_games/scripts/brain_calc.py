#!/usr/bin/env python3
"""Script to start calc game."""

from brain_games import starter
from brain_games.games import game_calc


def main():
    """Start game_calc()."""
    starter.start(game_calc)


if __name__ == '__main__':
    main()