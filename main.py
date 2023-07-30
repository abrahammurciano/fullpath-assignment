#!/usr/bin/env python3

from argparse import ArgumentParser

from sort_paragraph import sort_paragraph


def main():
    """A command-line interface for the sort_paragraph function."""
    parser = ArgumentParser(
        description="Sort the words in the given paragraph in ascending order, but sorted according to the order of the hebrew alphabet."
    )
    parser.add_argument(
        "paragraph",
        help="The paragraph to sort. If not given, read from stdin.",
        nargs="*",
    )
    paragraph = parser.parse_args().paragraph or input("Enter a paragraph to sort:\n")
    paragraph = paragraph if isinstance(paragraph, str) else " ".join(paragraph)
    print(sort_paragraph(paragraph))


if __name__ == "__main__":
    main()
