sec = int(input("Enter a lot of seconds: "))

min = sec // 60
temp_sec = min * 60
sec -= temp_sec

print(f"mins - {min} and secs - {sec}")