number = int(input("Enter a number: "))
summ = 0

if number % 7 == 0:
    print("MAGIC NUMBER")
else:
    summ = sum(map(int, str(number)))
    print(f"Summ of digits {summ}")
