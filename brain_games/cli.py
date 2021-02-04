#!/usr/bin/env python3
"""A user interaction module.

Imports input library.
"""

import prompt


def welcome_user():
    """Greets user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!').format(name)
