from datetime import datetime, date, timedelta

today = date.today()
now = datetime.now()

print(today - timedelta(days=5))

print(today - timedelta(days=1))
print(today)
print(today + timedelta(days=1))

print(now.replace(microsecond=0))

d1 = datetime(2024, 1, 1)
d2 = datetime(2024, 3, 15)
print((d2 - d1).total_seconds())
