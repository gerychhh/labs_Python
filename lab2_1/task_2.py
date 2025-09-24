from collections import Counter

myList = list(map(float, input("Enter a list: ").split()))

myList_count = Counter(myList)
myList_unique =[]
myList_not_unique =[]
myList_chet = []
myList_net_chet = []
myList_float = []
myList_ = []

print(myList_count)

for i, c in myList_count.items():
    if c == 1:
        myList_unique.append(i)

print(f"unique: {myList_unique}")

for i, c in  myList_count.items():
    if c > 1:
        myList_not_unique.append(i)

print(f"not_unique: {myList_not_unique}")

for i in myList:
    if i % 2 == 0:
        myList_chet.append(i)
print(f"chet: {myList_chet}")

for i in myList:
    if i % 2 != 0:
        myList_net_chet.append(i)
print(f"net_chet: {myList_net_chet}")

for i in myList:
    if i < 0:
        myList_.append(i)
print(f"numbers < 0: {myList_}")

for i in myList:
    if isinstance(i, float):
        myList_float.append(i)
print(f"float: {myList_float}")

summ = 0

for i in myList:
    if i % 5 == 0:
        summ += i
print(f"summ %5: {summ}")

print(f"Max in your list {max(myList)}")
print(f"Min in your list {min(myList)}")




