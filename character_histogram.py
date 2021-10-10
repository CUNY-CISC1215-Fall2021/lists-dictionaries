# Produce a histogram showing how frequently each letter of the alphabet is used in English

# To approximate English character frequency, we'll use the crossword puzzle dataset:
infile = open('words.txt')

# To compute the word usage histogram, we'll collect the counts of individual
# characters in our dataset. We'll store these counts in a dictionary, which
# will map each character to the number of times we encountered it.
counts = {}

# For each word in the dataset:
for word in infile:
    # Strip the word to remove newlines and other extra whitespace
    word = word.strip()

    # Iterate again - this time, over each character in the word:
    for character in word:
        # If we have never encountered this character before, we need to
        # add it to our character count dictionary. Give it an initial
        # count of 0
        if character not in counts:
            counts[character] = 0
        
        # Now increment the count for the character we just encountered
        counts[character] += 1

# Finally, print a summary. Vowels are likely the most commonly encountered,
# and 'e' is probably the most common:
print(counts)
