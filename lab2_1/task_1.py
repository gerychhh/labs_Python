from collections import Counter

text = input("Enter a string: ")
words = text.lower().split()
library_of_words = Counter(words)

print(library_of_words)
