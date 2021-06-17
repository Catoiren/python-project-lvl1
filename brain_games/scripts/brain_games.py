#!/usr/bin/env/ python3
"""Start games module."""

from brain_games import cli


def main():
    """Greet user."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user('May I have your name? ')
    print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    main()
