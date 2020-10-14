# Created by Noel Willems: a text cloud in Python

# Read in exclude file - probably in an array (list in Python)
excludeFile = open("exclude.txt")
rawWords = excludeFile.read().split()
print(rawWords)
# Read in input file and store cleaned individual words and their word counts, IGNORING excluded words

# Sort input words/values by value: most common -> least common

# Get top 50 of the sorted words/values

# Alphabetize the top 50

# Compute the size factor

# Write out HTML, varying sizes based on each word's size factor and randomizing the colors