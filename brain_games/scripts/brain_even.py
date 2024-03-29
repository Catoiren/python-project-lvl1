#!/usr/bin/env python3
"""Script to start even game."""

from brain_games import starter
from brain_games.games import even


def main():
    """Launch game_even()."""
    starter.launch(even)


if __name__ == '__main__':
    main()
