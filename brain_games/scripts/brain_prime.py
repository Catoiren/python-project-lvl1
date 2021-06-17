#!/usr/bin/env python3
"""Script to start brain_prime game."""

from brain_games import starter
from brain_games.games import game_prime


def main():
    """Launch game_prime()."""
    starter.launch(game_prime)


if __name__ == '__main__':
    main()
