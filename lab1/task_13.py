import random

secret = random.randint(1, 100)

while True:
    choice = int(input("Угадай число от 1 до 100: "))
    if choice < secret:
        print("Больше")
    elif choice > secret:
        print("Меньше")
    else:
        print("Угадал")
        break
