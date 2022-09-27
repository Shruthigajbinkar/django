import datetime
import calender
m, d, y = map(int, input().split())
input_date=datetime.date(y, m, d)
print('calender.day_name[input_date.weekday()].upper()')
