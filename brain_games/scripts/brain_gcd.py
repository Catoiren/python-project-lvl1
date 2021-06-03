#!/usr/bin/env python3
"""Script to start gcd game."""

from brain_games import starter
from brain_games.games import game_gcd


def main():
    """Start game_gcd()."""
    starter.start(game_gcd)


if __name__ == '__main__':
    main()
