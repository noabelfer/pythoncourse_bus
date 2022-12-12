import random

from busbest import schedule


class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, list_stops: list):
        self._bus_schedule = {}
        self._destination: str = destination
        self._line_number: int = line_number
        self._list_stops: list = list_stops
        self._origin: str = origin


    def __str__(self) -> str:
        st =str(self._line_number) + " " + self._destination + " " + str(self._list_stops)
        return st
        #return str(self.line_number + " " + self.origin + " " + self.destination + " " + str(self.list_stops) )

    def display_r(self):
        print(self.__str__())
        for s in self._bus_schedule:
            print(self._bus_schedule[s])


    def update_route(self, line_number, origin, destination, list_stops):
        for self.line_number is line_number:
            self._origin = origin
            self._destination = destination
            self._list_stops = list_stops


    def add_schedule(self, origin_time:int, destination_time:int, driver_name:str):
        s = schedule.ScheduledRides(origin_time, destination_time, driver_name)
        id:int = int(random.randrange(1,1000))
        print(id)
        self._bus_schedule[id] = s



a = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
a.add_schedule(9,10,'noa')
print(a)