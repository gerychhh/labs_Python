from collections import Counter

myList = list(map(float, input("Enter a list: ").split()))

myList_count = Counter(myList)

for i, c in myList_count.items():
    if c != 1:
        myList.remove(i)
print(f"unique list: {myList}")