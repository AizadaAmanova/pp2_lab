from datetime import datetime, timedelta

today = datetime.now()
new_data = today - timedelta(days = 5)

print("Current data:", today)
print("Date 5 days ago:", new_data)