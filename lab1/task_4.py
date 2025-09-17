cash = int(input("Enter your cash: "))
cash_temp = cash

banknots = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}

banknots[100] = cash_temp // 100
cash_temp -= banknots[100]*100

banknots[50] = cash_temp // 50
cash_temp -= banknots[50]*50

banknots[20] = cash_temp // 20
cash_temp -= banknots[20]*20

banknots[10] = cash_temp // 10
cash_temp -= banknots[10]*10

banknots[5] = cash_temp // 5
cash_temp -= banknots[5]*5

banknots[2] = cash_temp // 2
cash_temp -= banknots[2]*2

banknots[1] = cash_temp // 1
cash_temp -= banknots[1]

print(f"БАНКНОТА : КОЛИЧЕСТВО // {banknots}")