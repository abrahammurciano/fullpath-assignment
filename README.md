# Fullpath Home Assignment Solution

The function `sort_paragraph` (in `sort_paragraph.py`) sorts the words in a given paragraph in ascending order, but sorted according to the order of the hebrew alphabet.

You can view this document as well as all the code on [GitHub](https://github.com/abrahammurciano/fullpath-assignment) and on [repl.it](https://replit.com/@AbrahamMurciano/FullpathAssignment).

## Usage

You can follow along locally on your machine, or you can do it all on repl.it. If you do want to run it locally, please make sure to use Python 3.10+, though it should work just as well on any recent version.

### With the interpreter

To call the function from the python interpreter, launch `python` from the same directory as `sort_paragraph.py`, then import the function and call it as follows.

```python
>>> from sort_paragraph import sort_paragraph
>>> sort_paragraph("Roads? Where we're going we don't need roads.")
'going dont need Roads roads Where we were'
```

### From the command line

You can also directly run `main.py`. If you're following along on repl.it, you can just click the green run button.

It will prompt you to enter a paragraph to sort.

```
$ python main.py
Enter a paragraph to sort:
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
adipiscing aliqua amet do dolor dolore tempor labore Lorem magna sit sed incididunt ipsum ut consectetur et elit eiusmod
```

Or you can provide the paragraph to sort as a command line argument and avoid the prompt.

```
$ python main.py 'The quick brown fox jumps over the lazy dog.'
brown dog jumps The the lazy quick fox over
```

### With pytest

I have provided a few test cases in `tests.py` which you can run with pytest.

```
$ pytest tests.py
```

## Algorithm

The way the code works is as follows.

* First, the paragraph is stripped of punctuation using a regular expression to find and replace anything that isn't a letter or a space.
* Then the paragraph is split on spaces into a list of words, and duplicates are removed. (Note, "The" and "the" are *not* considered the same. They will appear in the order that they first appeared in the input.)
* Each word in the list is then converted into a tuple of indices matching each letter's position in the alphabet. For example, the word "hello" would become `(4, 23, 11, 11, 25)`.
* The words are then sorted according to the order of the tuples. Python takes care of sorting the tuples.
* Finally the words are joined back together into a string and returned.
