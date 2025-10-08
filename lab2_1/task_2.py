myList = list(map(float, input("Введите список: ").split()))

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

print(f"уникальные значения: {myList_unique}")
print(f"неуникальные значения: {myList_not_unique}")

for num in myList:
    if num.is_integer():
        if int(num) % 2 == 0:
            myList_chet.append(num)
        else:
            myList_net_chet.append(num)

print(f"чётные значения: {myList_chet}")
print(f"нечётные значения: {myList_net_chet}")

for num in myList:
    if num < 0:
        myList_negative.append(num)
print(f"значения меньше нуля: {myList_negative}")

for num in myList:
    if isinstance(num, float):
        myList_float.append(num)
print(f"числа с плавующей точкой: {myList_float}")

summ = 0
for num in myList:
    if num.is_integer() and int(num) % 5 == 0:
        summ += num
print(f"сумма всех чисел кратных 5: {summ}")

print(f"максимальное значение в списке {max(myList)}")
print(f"минимальное значение в списке {min(myList)}")
