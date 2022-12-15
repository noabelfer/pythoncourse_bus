import datetime
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
        return f'line_number: {self._line_number} \n origin: {self.origin} \n destination: {self.destination} \n list_stops: {self.list_stops} \n bus_schedule: {self._bus_schedule}'


    def __repr__(self):
        return self.__str__()

    # def search_route(self, k,v) -> bool:
    #     current = False
    #     print(self.list_stops, 'lk')
    #     match(k):
    #         case 'origin':
    #             current = (self.origin == v)
    #         case 'destination':
    #             current = (self.destination == v)
    #         case 'stop':
    #             current =  (v in self.list_stops)
    #     return current


    def search_origin(self, origin) ->int:
        return self.origin == origin



    # def get_dict(self, origin_time ,destination_time, driver_name):
    #     my_dict = {}
    #     my_dict['origin'] = self.origin
    #     my_dict['destination'] = self.destination
    #     my_dict['list_stops'] = self.list_stops
    #     for d in self._bus_schedule:
    #         print(self._bus_schedule, d)
    #         my_dict['bus_schedule'][d] = self._bus_schedule[d].get_dict_s()
    #     print (my_dict)
    #     return my_dict



    # def get_schedule(self):
    #     return self._bus_schedule

    def display_r(self):
        print(self.__str__())
        for s in self._bus_schedule:
            print(self._bus_schedule[s])

    # def display_r(self):
    #     print(self.__str__())
    #     for s in self._bus_schedule:
    #         print(BusRoute[s].get_dict_s())


    # def update_route(self, origin, destination, list_stops:list):
    #     # for BusRoute[line_number]:
    #     self.origin = origin
    #     self.destination= destination
    #     self.list_stops = list_stops


    #create an object of type ScheduledRides:
    #adds the object to self._bus_schedule = {}
    def add_schedule(self, origin_time:int, destination_time:int, driver_name:str):
        s = schedule.ScheduledRides(origin_time, destination_time, driver_name)
        id:int = int(random.randrange(1,1000))
        self._bus_schedule[id] = origin_time, destination_time, driver_name

    #adds delay to list of delays in self._bus_schedule by schedule class:
    def add_delay(self, id, delay_min):
        self._bus_schedule[id].add_delay(delay_min)


    def get_sc_dict(self):
        print(self._bus_schedule)


# a = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
# b = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
# c = BusRoute(5,'bal', 'rm', ['aaa','bbb'])
# a.add_schedule(3,4,'noa')
# a.add_schedule(4,5,'noaded')
# print(a.get_schedule())
#
# a.add_schedule(9,11,'noa')
# # a.search_route('origin', 'tkklko')
#
# print(a.get_dict(9,11,'noa'))

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
