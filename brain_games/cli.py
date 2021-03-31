#!/usr/bin/env/ python3
"""Welcoming user module."""

import prompt


def welcome_user(question):
    """Ask user's name.

    Args:
        question: str

    Returns:
        return: str
    """
    return prompt.string(question)


if __name__ == '__main__':
    welcome_user()
