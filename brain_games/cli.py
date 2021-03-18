#!/usr/bin/env/  python3
"""Welcoming user module."""

import prompt


def welcome_user():
    """Ask user's name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))  # noqa: WPS421


if __name__ == '__main__':
    welcome_user()
