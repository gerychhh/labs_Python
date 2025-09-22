while True:

    password = input("Введите пароль: ")
    if len(password) < 16:
        print("Слишком короткий")
    elif not password.isalpha() and not password.isdigit():
        print("Надёжный пароль")
        break
    else:
        print("Ненадёжный пароль")