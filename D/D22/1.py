# Implement a simple class DateIterator that should be initialized
# with a date and implements iterator protocol (__iter__ and __next__ method)
# that on every iteration returns the next date up until the end of the month.

from calendar import  monthrange
from datetime import datetime


class DateIterator:

    def __init__(self, date: str):
        self.date = datetime.strptime(date, "%d-%m-%Y").date()
        self.days_in_month = monthrange(self.date.year, self.date.month)[1]
        print(self.days_in_month)


    def __iter__(self):
        self.start = int(self.date.day)
        return self

    def __next__(self):
        if self.start < self.days_in_month:
            self.start += 1
        else:
            raise StopIteration
        return datetime(day=self.start, month=self.date.month, year=self.date.year).date()


try:
    date = input("insert date")
    for c in DateIterator(date):
        print(c)

except Exception:
    print(" ")

