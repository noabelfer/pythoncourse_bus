# date_input = "Mon, Dec 19, 2022 10:00 PM"
from datetime import datetime, date, timedelta

def time_left(date_input):

    try:
        td =  datetime.strptime(date_input, "%a, %b %d, %Y %I:%M %p") - datetime.utcnow()
        return td
    except ValueError:
        return None

a = time_left("Mon, Dec 19, 2022 10:00 PM")
print(a)
