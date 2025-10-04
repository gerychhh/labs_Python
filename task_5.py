def cache(func):
    saved = {}
    def wrapper(*args):
        if args not in saved:
            saved[args] = func(*args)
        return saved[args]
    return wrapper

@cache
def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

x = int(input("Введите основание степени: "))
y = int(input("Введите показатель степени: "))
print("Результат возведения в степень:", power(x, y))
print("Повторный вызов (значение берётся из кэша):", power(x, y))
