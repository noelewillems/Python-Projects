# Created by Noel Willems: a text cloud in Python
# Sources listed in respective lines.

from collections import Counter
import string
import sys
import random
# Read in exclude file - probably in an array (list in Python)
excludeFile = open(sys.argv[2])
excludedWords = excludeFile.read().split()
# Read in input file and store cleaned individual words and their word counts, IGNORING excluded words
# Source: https://docs.python.org/3/library/stdtypes.html#str
punc = set(string.punctuation)
i = 0
wordsList = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        for word in line.split():
            word = word.lower()
            if word not in excludedWords:
                word = ''.join(ch for ch in word if ch not in punc)
                if word not in excludedWords and len(word) != 0:
                    wordsList.append(word)

# Use counter to create list of tuples, with word as first tuple element and frequency as second tuple element
# Source: https://docs.python.org/2/library/collections.html
words = Counter(wordsList)
# Get 50 most common words
top50 = words.most_common(50)
# Calculate size range
# Source: https://www.tutorialspoint.com/python/python_tuples.htm
sizeRange = top50[0][1] - top50[49][1]
# Sort alphabetically
# Source: https://docs.python.org/3/howto/sorting.html
top50 = sorted(top50, key=lambda w:w[0])
cnt = 0
with open(sys.argv[3], 'w') as file:
    file.write("<!DOCTYPE html><html><body>")
    for i in top50:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        file.write("<span style = \"font-size:" + str((sizeRange * top50[cnt][1])/100) + "%; color: rgb(" + str(r) + ", " + str(g) + ", " + str(b) + ")\">" + top50[cnt][0] + " </span> \n")
        cnt += 1
    file.write("\n</body></html>")
