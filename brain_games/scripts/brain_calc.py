#!/usr/bin/env python3
"""Script to start calc game."""

from brain_games import starter
from brain_games.games import calc


def main():
    """Launch game_calc()."""
    starter.launch(calc)


if __name__ == '__main__':
    main()
