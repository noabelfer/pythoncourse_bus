from datetime import time
import random

from busbest import schedule
from busbest.schedule import ScheduledRides


class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, list_stops: list):

        self.origin = origin
        self.destination = destination
        self.list_stops = list_stops
        self._bus_schedule = {}
        self._line_number: int = line_number


    def __str__(self) -> str:
        return f'line_number: {self._line_number} \n origin: {self.origin} \n destination: {self.destination} \n list_stops: {self.list_stops} \n bus_schedule: {self._bus_schedule.__repr__()}'


    def __repr__(self):
        return self.__str__()



    def search_origin(self, origin) -> bool:
        return self.origin == origin

    def search_destination(self, destination) -> bool:
        return self.destination == destination

    def search_station(self, station) -> bool:
        return station in self.list_stops

    def add_delay(self, delay_min):
        return self._bus_schedule[id].add_delay(delay_min)



    # def get_schedule(self):
    #     return self._bus_schedule

    def display_r(self):
        print(self.__str__())
        for s in self._bus_schedule:
            print(self._bus_schedule[s])

    def present_sched(self):
        return self._bus_schedule

    # def update_route(self, origin, destination, list_stops:list):
    #     # for BusRoute[line_number]:
    #     self.origin = origin
    #     self.destination= destination
    #     self.list_stops = list_stops



    #adds the object to self._bus_schedule = {}
    def add_schedule(self, origin_time:time, destination_time:time, driver_name:str):
        s = schedule.ScheduledRides(origin_time, destination_time, driver_name)
        id:int = int(random.randrange(1,1000))
        self._bus_schedule[id] = origin_time, destination_time, driver_name

    #adds delay to list of delays in self._bus_schedule by schedule class:
    def add_delay(self, delay, id):
        # d = schedule.ScheduledRides(delays)
        self._bus_schedule[id] = delay


    # def get_sc_dict(self):
    #     print(self._bus_schedule.__class_getitem__(ScheduledRides.__repr__()))


# a = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
# # # b = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
# # # c = BusRoute(5,'bal', 'rm', ['aaa','bbb'])
# a.add_schedule(3,4,'noa')
# print(a.add_delay(4,5))
# print(a.__repr__())
# a.add_schedule(4,5,'noaded')
# print(a.get_schedule())
#
# a.add_schedule(9,11,'noa')
# # a.search_route('origin', 'tkklko')
#
# print(a.get_sc_dict())

# print(a.my_s_dict)
# a.__str__()
# #
# for i in d['bus_schedule']:
#     a.add_delay(i,5)
# print(a.get_dict(),'ooo')
# a.display_r()




# a.search_route('origin', 'telaviv')

# print(a)
# a.add_schedule(9,10,'noa')
# s.search('origin','telaviv')
