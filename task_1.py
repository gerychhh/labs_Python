def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            sub = lst.pop(i)
            for j in range(len(sub) - 1, -1, -1):
                lst.insert(i, sub[j])
        else:
            i += 1

user_list = eval(input())
flatten_list(user_list)
print(user_list)
