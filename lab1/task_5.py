number = int(input("Enter a number: "))

if number % 7 == 0:
    print("MAGIC NUMBER")
else:
    summ = 0
    n = number
    while n > 0:
        summ += n % 10
        n //= 10
    print(f"Summ of digits {summ}")
