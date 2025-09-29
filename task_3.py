from datetime import datetime
from traceback import print_tb


def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()} | {func.__name__} | args={args}, kwargs={kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("calls.log")
def add_numbers(x, y):
    return x + y

a = int(input("Слогаемое A"))
b = int(input("Слогаемое B"))
print("Ответ A+B")
print(add_numbers(a, b))
