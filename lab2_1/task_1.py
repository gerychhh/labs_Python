text = input("Введите строку: ")
words = text.lower().split()

library_of_words = {}

for word in words:
    if word in library_of_words:
        library_of_words[word] += 1
    else:
        library_of_words[word] = 1

print(f"(Слово : количество повторений) {library_of_words}")
