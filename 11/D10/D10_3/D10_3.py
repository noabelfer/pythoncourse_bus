# Write a function that receives a date in format dd-mm-yy,
# and returns a date of the upcoming Friday as string in format: dd-mm-yyyy
from datetime import datetime, timedelta
import calendar


def get_friday(date_start: str) ->datetime:
    date1 = datetime.strptime(date_start,"%d-%m-%y").date()
    # print(date1.strftime("%d:%m:%y"))
    day,month, year = date1.strftime("%d"), date1.strftime("%m"), date1.strftime("%y")
    day_num = calendar.weekday(int(year), int(month), int(day))
    # print (day_num)
    delta_day:int = 4 - day_num
    # print(delta_day)
    get_date = (date1 + timedelta(delta_day))
    # print(get_date)
    end_date = get_date.strftime("%d-%m-%Y")
    return end_date

a = get_friday("20-12-22")
print(a)




