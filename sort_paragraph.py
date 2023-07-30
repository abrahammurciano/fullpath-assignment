import re
from typing import Iterable, Sequence


def sort_paragraph(paragraph: str) -> str:
    """Sort the words in the given paragraph in ascending order, but sorted according to the order of the hebrew alphabet.

    Args:
        paragraph: A paragraph of english text whose words to sort.

    Returns:
        A space-separated string of the sorted words (with all punctuation removed).
    """
    return " ".join(sort_words(extract_words(paragraph), "ABGDHVZJTYKLMNSIPXQRWUCEFO"))


def extract_words(paragraph: str) -> Iterable[str]:
    """Get all the words in the given paragraph."""
    return re.sub(r"[^a-zA-Z\s]", "", paragraph).split()


def sort_words(words: Iterable[str], alphabet: str) -> Sequence[str]:
    """Sort the given words in lexicographic order according to the given alphabet."""
    return sorted(
        words, key=lambda word: tuple(alphabet.index(letter) for letter in word.upper())
    )
