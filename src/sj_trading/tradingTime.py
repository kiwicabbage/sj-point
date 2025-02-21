# tradingTime.py
import datetime

def is_morning_or_afternoon():
    now = datetime.datetime.now().time()
    return datetime.time(9,5) < now < datetime.time(13,45)

def is_trading_hours():
    now = datetime.datetime.now()
    weekday = now.weekday()
    current_time = now.time()
    
    if weekday == 5 and current_time >= datetime.time(5, 0):
        return False
    if weekday == 6:
        return False
    if weekday == 0 and current_time < datetime.time(9,5):
        return False
    if datetime.time(5,0) <current_time < datetime.time(9, 5) or (datetime.time(13, 45) <= current_time < datetime.time(15, 10)):
        return False
    return True