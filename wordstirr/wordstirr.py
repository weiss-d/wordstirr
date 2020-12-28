"""
Base function for "stirring" a single word and a whole text.
"""

import random
from typing import List

import regex


def _process_word(word: str) -> str:
    """Randomize letter order in word leaving first and last letters in place.

    Parameters
    ----------
    word : str
        Normal word

    Returns
    -------
    str
        "Stirred" word

    """
    if len(word) <= 3:
        return word

    first_letter, *innards, last_letter = word
    random.shuffle(innards)
    return "".join([first_letter] + innards + [last_letter])


def text_stirr(input_string: str) -> str:
    """Stirrs every word in a given text.

    Parameters
    ----------
    input_string : str
        Text for processing (may contain line breaks and unicode symbols)

    Returns
    -------
    str
        Same text, but with stirred words.

    """
    text_list: List = []
    while input_string:
        split = regex.split(r"([^\p{L}]+)", input_string, maxsplit=1)
        text_list.append(_process_word(split[0]))
        text_list.append(split[1])
        input_string = split[2]
    return "".join(text_list)
