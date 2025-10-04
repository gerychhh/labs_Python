myStr = input("input list: ")

myList = list(myStr)

myCount = {}

myStr = ""

##print(myList)

for i in myList:
    if i not in myCount:
        myCount[i] = 1
    else:
        myCount[i] += 1

for i, c in myCount.items():
    myStr += str(i) + str(c)

print(f"your short string: {myStr}")