def merge_sorted_list(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result

list1 = list(map(int, input("Введите первый отсортированный список (через пробел): ").split()))
list2 = list(map(int, input("Введите второй отсортированный список (через пробел): ").split()))
print("Объединённый отсортированный список:", merge_sorted_list(list1, list2))
