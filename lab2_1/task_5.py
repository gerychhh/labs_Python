myString1 = input("Введите строку 1: ")
myString2 = input("Введите строку 2: ")
if(sorted(myString1.lower()) == sorted(myString2.lower())):
    print("Являются анаграммами")
else:
    print("Не являются анаграммами")