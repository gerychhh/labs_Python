def merge_dicts(d1, d2):
    for k, v in d2.items():
        if k in d1 and isinstance(d1[k], dict) and isinstance(v, dict):
            merge_dicts(d1[k], v)
        else:
            d1[k] = v

dict_a = eval(input("Первый словарь: "))
dict_b = eval(input("Второй словарь: "))
merge_dicts(dict_a, dict_b)
print("Результат слияния:", dict_a)
