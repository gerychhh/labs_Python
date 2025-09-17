while True:

    password = input("Enter your password: ")
    if len(password) < 16:
        print("Password must be at least 16 characters")
    elif not password.isalpha() and not password.isdigit():
        print("Надёжный пароль")
        break
    else:
        print("Ненадёжный пароль")