myString1 = input("Enter a string1: ")
myString2 = input("Enter a string2: ")

if(sorted(myString1.lower()) == sorted(myString2.lower())):
    print("True")
else:
    print("False")