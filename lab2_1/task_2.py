myList = list(map(float, input("Enter a list: ").split()))

myList_count = {}
for num in myList:
    myList_count[num] = myList_count.get(num, 0) + 1

myList_unique = []
myList_not_unique = []
myList_chet = []
myList_net_chet = []
myList_float = []
myList_negative = []

print(myList_count)

for num, count in myList_count.items():
    if count == 1:
        myList_unique.append(num)
    else:
        myList_not_unique.append(num)

print(f"unique: {myList_unique}")
print(f"not_unique: {myList_not_unique}")

for num in myList:
    if num.is_integer():
        if int(num) % 2 == 0:
            myList_chet.append(num)
        else:
            myList_net_chet.append(num)

print(f"chet: {myList_chet}")
print(f"net_chet: {myList_net_chet}")

for num in myList:
    if num < 0:
        myList_negative.append(num)
print(f"numbers < 0: {myList_negative}")

for num in myList:
    if isinstance(num, float):
        myList_float.append(num)
print(f"float: {myList_float}")

summ = 0
for num in myList:
    if num.is_integer() and int(num) % 5 == 0:
        summ += num
print(f"summ %5: {summ}")

print(f"Max in your list {max(myList)}")
print(f"Min in your list {min(myList)}")
