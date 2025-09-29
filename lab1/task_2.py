str = input("Enter a string: ")
letters = ["a", "e", "i", "o", "u"]

##тк нельзя циклы, такая реализация
str = str.replace("a", "")
str = str.replace("e", "")
str = str.replace("i", "")
str = str.replace("o", "")
str = str.replace("u", "")

print(f"your string without a, e, i, o, u: {str}")