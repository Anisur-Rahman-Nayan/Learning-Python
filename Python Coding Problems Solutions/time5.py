from datetime import datetime

now = datetime.now()

year = now.strftime("%Y")
print(year)

month = now.strftime("%m")
print(month)

day = now.strftime("%d")
print(day)

time = now.strftime("%H : %M : %S")
print(time)

