from datetime import time
import random

from busbest import schedule
from busbest.schedule import ScheduledRides


class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, list_stops: list):

        self._origin = origin
        self._destination = destination
        self._list_stops = list_stops
        self._bus_schedule = {}
        self._line_number: int = line_number


    def __str__(self) -> str:
        return f'line_number: {self._line_number} \n origin: {self._origin} \n destination: {self._destination} \n list_stops: {self._list_stops} \n bus_schedule: {self._bus_schedule}'


    def __repr__(self):
        return self.__str__()



    def _search_origin(self, origin) -> bool:
        return self._origin == origin

    def _search_destination(self, destination) -> bool:
        return self._destination == destination

    def _search_station(self, station) -> bool:
        return station in self._list_stops


    #adds delay to list of delays in self._bus_schedule by schedule class:
    def _add_delay(self, delay, id):
        # d = schedule.ScheduledRides(delays)
        self._bus_schedule[id] = delay


    def _display_r(self):
        print(self.__str__())
        for s in self._bus_schedule:
            print(self._bus_schedule[s])

    def _present_sched(self):
        return self._bus_schedule.__repr__()


    #adds the object to self._bus_schedule = {}
    def _add_schedule(self, origin_time:str, destination_time:str, driver_name:str):
        id:int = int(random.randrange(1,1000))
        self._bus_schedule[id] = origin_time, destination_time, driver_name


    def _get_sc_dict(self):
        print(self._bus_schedule._origin)





