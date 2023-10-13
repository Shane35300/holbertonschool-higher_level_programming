#!/usr/bin/python3
"""
This function  prints a text with 2 new lines
 after each of those characters:
   .? and :
    there must be 2 new lines after each splitting
"""


def text_indentation(text):
    """
    text is the text that I print
    separators = ".", ":", "?"
    """
    if text is None:
        raise TypeError("text must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    detector = 0
    for i in range(len(text)):
        if text[i] == " " and detector == 0:
            continue
        else:
            print(text[i], end="")
            detector = 1
        if text[i] in ".:?":
            print("\n")
            detector = 0
