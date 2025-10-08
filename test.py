import random
import time

def Timer(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        total_time = end - start
        print(total_time)
    return wrapper




a = random.randint(0,100)

@Timer
def rand():
    while True:
        if a == random.randint(0,100):
            break
        else:
            print("1")


rand()