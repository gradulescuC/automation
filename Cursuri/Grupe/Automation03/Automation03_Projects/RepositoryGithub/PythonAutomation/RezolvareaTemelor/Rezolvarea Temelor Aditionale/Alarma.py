from datetime import time, timedelta, datetime
from pytz import timezone

ustz = datetime.now(timezone('US/Eastern')).hour
print("Current hour in America is: ", ustz)

wake_hour = int(input('Enter your waking hour: '))
while wake_hour < 0 or wake_hour > 24:
    wake_hour = int(input("Invalid hour, please try again: "))
if wake_hour == ustz:
    for i in range(10):
        print('ding')
    print(f"It's {wake_hour} o'clock, wake up!")
else:
    print(f'Current local hour in the timezone is {ustz} ')

