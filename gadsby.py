# Gadsby is a novel published in 1939, where the author deliberately chose
# to write it without using the letter "e" as a challenge to himself:
#
# https://en.wikipedia.org/wiki/Gadsby_(novel)
#
# This file will use the nondestructive map, filter, and reduce list manipulation
# patterns to look through the words.txt crossword dataset to make an informed guess
# about how many words the author might have had available to write this novel.
#
# To do this, we need to:
#   1. Load the words.txt dataset
#   2. Perform a mapping operation to remove newlines and other leading/trailing spaces
#   3. Perform a filter operation to remove words containing the letter 'e'
#   4. Perform a reduction operation to produce summary statistics

infile = open('words.txt')

# Load all words: note we cast the infile to a list. This effectively loads the entire
# dataset into memory, with one line per list element!
lines = list(infile)

# Map operation: strip all characters in the word list. Put the result in a new list
# called "cleaned." All elements in the "cleaned" list will not have extra whitespace.
cleaned = []
for line in lines:
    cleaned.append(line.strip())

# Filter operation: Created a new list "filtered" which contains only words that do
# not contain the letter "e"
filtered = []
for word in cleaned:
    if 'e' not in word:
        filtered.append(word)

# Reduce operation: Reduce the entire "filtered" list to a small number of summary
# statistics. Let's calculate how many eligible words there are, and how long the longest
# available word is.
length = 0
longest = 0
for word in filtered:
    if len(word) > longest:
        longest = len(word)
    length += 1

print('original list:', len(lines))
print('filtered list', length)
print('Longest non-e word', longest)

# Some notes:
#   1. It would arguably be more efficient to do all of these in a single loop, instead
#      of breaking them into separate loops. But sometimes the clarity of breaking your
#      program into several small, easy-to-understand steps is better than maximizing
#      efficiency!
#   2. Python includes several ways to make these operations nicer, including some methods
#      that take advantage of its functional programming features. We will look at these
#      later.