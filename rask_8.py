import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения функции: {(end - start)*1000:.3f} мс")
        return result
    return wrapper

@timing
def big_sum(n):
    s = 0
    i = 0
    while i < n:
        s += i
        i += 1
    return s

num = int(input("Введите число, до которого нужно суммировать: "))
print("Сумма чисел:", big_sum(num))
