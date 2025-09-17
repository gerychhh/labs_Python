str = input("Enter a string: ")
letters = ["a", "e", "i", "o", "u"]

##тк нельзя циклы, такая реализация
str = str.replace(letters[0], "")
str = str.replace(letters[1], "")
str = str.replace(letters[2], "")
str = str.replace(letters[3], "")
str = str.replace(letters[4], "")

print(f"your string without a, e, i, o, u: {str}")