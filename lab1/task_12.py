base_price = 24.99
free_minutes = 60
free_sms = 30
free_mb = 1024

price_per_minute = 0.89
price_per_sms = 0.59
price_per_mb = 0.79
tax_rate = 0.02


minutes = int(input("Израсходованные минут: "))
sms = int(input("Количество отправленных SMS: "))
mb = int(input("Количество использованных МБ интернета: "))


total = base_price
print(f"Базовая стоимость тарифа: {base_price:.2f} руб.")


if minutes > free_minutes:
    extra_minutes = (minutes - free_minutes) * price_per_minute
    total += extra_minutes
    print(f"Доп. минуты: {extra_minutes:.2f} руб.")


if sms > free_sms:
    extra_sms = (sms - free_sms) * price_per_sms
    total += extra_sms
    print(f"Доп. SMS: {extra_sms:.2f} руб.")


if mb > free_mb:
    extra_mb = (mb - free_mb) * price_per_mb
    total += extra_mb
    print(f"Доп. интернет: {extra_mb:.2f} руб.")


tax = total * tax_rate
total_with_tax = total + tax
print(f"Налог (2%): {tax:.2f} руб.")


print(f"Итого к оплате: {total_with_tax:.2f} руб.")
