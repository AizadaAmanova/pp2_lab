from datetime import datetime, timedelta

today = datetime.now()
date = today - timedelta(days = 2)

difference = (today - date).total_seconds()

print("Difference:", difference)