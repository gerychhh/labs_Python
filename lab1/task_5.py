number = input("Enter a number: ")
total = 0

if int(number) % 7 == 0:
    print("MAGIC NUMBER")
else:
    summ = sum(map(int, str(number)))
    print(f"Summ of digits {total}")
