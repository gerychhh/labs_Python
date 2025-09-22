
str = input("Enter your ip: ")
list = str.split(".")

if all(int(x)>=0 for x in list) and all(int(x)<=255 for x in list):
    print("Good ip")
else:
    print("Bad ip")