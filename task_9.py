def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for a, t in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError("Неверный тип аргумента")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
print("Результат сложения:", add(x, y))
