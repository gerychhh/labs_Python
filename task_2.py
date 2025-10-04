def merge_dicts(d1, d2):
    for k, v in d2.items():
        if k in d1 and isinstance(d1[k], dict) and isinstance(v, dict):
            merge_dicts(d1[k], v)
        else:
            d1[k] = v

dict_a = eval(input("Введите первый словарь (пример: {'a':1,'b':{'c':2}}): "))
dict_b = eval(input("Введите второй словарь: "))
merge_dicts(dict_a, dict_b)
print("Результат слияния:", dict_a)
