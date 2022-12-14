from calendar import  monthrange
from datetime import datetime
from datetime import timedelta


class DateIterator:

    def __init__(self, date: str):
        self.date = datetime.strptime(date, "%d-%m-%Y").date()

    def __iter__(self):
        return self

    def __str__(self):
        return(f' date:{self.date}')

    def __next__(self):
        days_in_month = monthrange(self.date.year, self.date.month)[1]
        if self.date.day == days_in_month:
            raise StopIteration

        # if self.date.day <= self.days_in_month:
        self.date += timedelta(days = 1)

        return self
        # else:
        #     raise StopIteration



# datetime.date(year, month, last_day)
a = DateIterator("12-10-2020")
# print(next(a))
for d in a:
    print(d)