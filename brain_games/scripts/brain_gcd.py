#!/usr/bin/env python3
"""Script to start gcd game."""

from brain_games import starter
from brain_games.games import gcd


def main():
    """Launch game_gcd()."""
    starter.launch(gcd)


if __name__ == '__main__':
    main()
