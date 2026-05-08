import datetime


def reset_daily_minutes(data):
    today = str(datetime.date.today())
    if data.get("last_reset") != today:
        data["total_minutes"] = 0
        data["last_reset"] = today
