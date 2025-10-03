cash = int(input("Enter your cash: "))
cash_temp = cash

h100 = cash_temp // 100
cash_temp -= h100 * 100

h50 = cash_temp // 50
cash_temp -= h50 * 50

h20 = cash_temp // 20
cash_temp -= h20 * 20

h10 = cash_temp // 10
cash_temp -= h10 * 10

h5 = cash_temp // 5
cash_temp -= h5 * 5

h2 = cash_temp // 2
cash_temp -= h2 * 2

h1 = cash_temp

print(f"To pay {cash} BYN you need:")
if h100 > 0:
    print(f"{h100} x 100 BYN")
if h50 > 0:
    print(f"{h50} x 50 BYN")
if h20 > 0:
    print(f"{h20} x 20 BYN")
if h10 > 0:
    print(f"{h10} x 10 BYN")
if h5 > 0:
    print(f"{h5} x 5 BYN")
if h2 > 0:
    print(f"{h2} x 2 BYN")
if h1 > 0:
    print(f"{h1} x 1 BYN")
