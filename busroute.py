from random import random

from bus import schedule


class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, list_stops: list):
        self.__bus_schedule = {}
        self.destination: str = destination
        self.line_number: int = line_number
        self.list_stops: list = list_stops
        self.origin: str = origin


    def __str__(self) -> str:
        st =str(self.line_number) + " " + self.destination + " " + str(self.list_stops)
        return st
        #return str(self.line_number + " " + self.origin + " " + self.destination + " " + str(self.list_stops) )

    def display_r(self):
        print(self.__str__())
        for s in self.__bus_schedule:
            print(self.__bus_schedule[s])



    def update_route(self, line_num, origin=None, destination=None, list_stops=None):
        pass

    def add_schedule(self, origin_time:int, destination_time:int, driver_name:str):
        s = schedule.ScheduledRides(origin_time, destination_time, driver_name)
        id = random
        self.__bus_schedule[id] = s


# a = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
# print(a)