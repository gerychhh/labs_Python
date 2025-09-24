myList = list(map(float, input().split()))
cacheList =myList
Max_number = 0.0
secondMax = 0.0

Max_number = max(myList)

cacheList.remove(Max_number)

print(max(myList))