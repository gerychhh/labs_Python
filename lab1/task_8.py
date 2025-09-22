str = input("Enter a string: ")

str = str.lower()

str_copy = "".join(reversed(str))

if str == str_copy:
    print("Палиндром")
else:
    print("Не палиндром")

