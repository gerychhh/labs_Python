def unique_elements(lst):
    result = []
    seen = set()
    def walk(x):
        for el in x:
            if isinstance(el, list):
                walk(el)
            else:
                if el not in seen:
                    seen.add(el)
                    result.append(el)
    walk(lst)
    return result

user_list = eval(input("Введите вложенный список (пример: [1,2,[3,[4]]]): "))
print("Уникальные элементы:", unique_elements(user_list))
