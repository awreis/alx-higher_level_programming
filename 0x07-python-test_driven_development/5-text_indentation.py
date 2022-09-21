#!/usr/bin/python
"""
Module 5-text_indentation
Defines a text-indentation function
"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'
    Args:
        text (string): The text to print
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
