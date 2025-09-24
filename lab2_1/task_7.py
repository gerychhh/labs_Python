from collections import Counter

myList = list(map(str, input("Enter a list: ").split()))

myList_count = Counter(myList)

myStr = ""

for i, c in myList_count.items():
    myStr += str(i)+str(c)

print("В виде ключ значение")
print(myList_count)
print("В виде строки")
print(myStr)