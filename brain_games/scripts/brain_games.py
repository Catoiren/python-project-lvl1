#!/usr/bin/env/ python3
"""Start games module."""

from brain_games.cli import welcome_user


def main():
    """Greet user."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
