from typing import NamedTuple

import pytest

from sort_paragraph import sort_paragraph


class Example(NamedTuple):
    paragraph: str
    expected: str


examples = [
    Example(
        paragraph="The quick brown fox jumps over the lazy dog.",
        expected="brown dog jumps The the lazy quick fox over",
    ),
    Example(
        paragraph="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        expected="adipiscing aliqua amet do dolor dolore tempor labore Lorem magna sit sed incididunt ipsum ut consectetur et elit eiusmod",
    ),
    Example(
        paragraph="Roads? Where we're going we don't need roads.",
        expected="going dont need Roads roads Where we were",
    ),
]


@pytest.mark.parametrize("paragraph,expected", examples)
def test_sort_paragraph(paragraph: str, expected: str):
    assert sort_paragraph(paragraph) == expected
