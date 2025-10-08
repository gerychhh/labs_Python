myStr = input("Введите список: ")

myList = list(myStr)

myCount = {}

newList =[]

for i in myList:
    if i not in myCount:
        myCount[i] = 1
    else:
        myCount[i] += 1


for i, c in myCount.items():
    if c == 1:
        newList.append(i)

myList = newList

print(f"Ваш новый список с уникальными значениями: {myList}")