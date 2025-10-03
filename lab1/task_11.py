day = int(input("Введите день рождения (число месяца): "))
month = int(input("Введите месяц рождения (номер месяца): "))

if (day >= 21 and month == 3) or (day <= 20 and month == 4):
    sign = "Овен"
elif (day >= 21 and month == 4) or (day <= 21 and month == 5):
    sign = "Телец"
elif (day >= 22 and month == 5) or (day <= 21 and month == 6):
    sign = "Близнецы"
elif (day >= 22 and month == 6) or (day <= 22 and month == 7):
    sign = "Рак"
elif (day >= 23 and month == 7) or (day <= 21 and month == 8):
    sign = "Лев"
elif (day >= 22 and month == 8) or (day <= 23 and month == 9):
    sign = "Дева"
elif (day >= 24 and month == 9) or (day <= 23 and month == 10):
    sign = "Весы"
elif (day >= 24 and month == 10) or (day <= 22 and month == 11):
    sign = "Скорпион"
elif (day >= 23 and month == 11) or (day <= 22 and month == 12):
    sign = "Стрелец"
elif (day >= 23 and month == 12) or (day <= 20 and month == 1):
    sign = "Козерог"
elif (day >= 21 and month == 1) or (day <= 19 and month == 2):
    sign = "Водолей"
elif (day >= 20 and month == 2) or (day <= 20 and month == 3):
    sign = "Рыбы"
else:
    sign = "Некорректная дата"

print("Ваш знак зодиака:", sign)
