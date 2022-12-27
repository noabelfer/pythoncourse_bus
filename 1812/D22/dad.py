import calendar
import datetime


class Mydate:
    def __init__(self, dt):
        self.__date = dt

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__end_of_month()):
            raise StopIteration
        self.__date += datetime.timedelta(days=1)
        return self

    def __str__(self):
        return str(self.__date)

    def __end_of_month(self):
        month = self.__date.month
        next_day = self.__date + datetime.timedelta(days=1)
        next_month = next_day.month
        return month != next_month


mydate = datetime.datetime(2022, 11, 24)
for d in Mydate(mydate):
    print(d)
