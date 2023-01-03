# Implement a function that gets a string that represents
# datetime in the following format: "2021-12-08, Wed, 10:00" and
# returns the name of the weekday 3 days after the received date.
# For example, for the input provided, the output should be: Saturday.
# Write 2 unit tests to test your function
from datetime import datetime, date, timedelta
from decorators import *


def days_want(date_input:str) -> str:

    try:
        date = datetime.strptime(date_input, "%Y-%m-%d,%a, %I:%M")
        get_day = date + timedelta(3)
        day_wanted = (get_day.strftime('%A'))
        return day_wanted
    except ValueError:
        return None


a = days_want("2021-12-08,Wed, 10:00")
print(a)






