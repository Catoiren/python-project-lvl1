#!/usr/bin/env python3
"""Run game module."""

import cli


def main():
    """Represent interaction between user and games.

    It welcomes user, then asks for name and welcomes by name.
    """
    print('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
