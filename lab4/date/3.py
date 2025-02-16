from datetime import datetime, timedelta

today = datetime.now()
microsecond = today.replace(microsecond = 0)

print("Current data:", today)
print(microsecond)
