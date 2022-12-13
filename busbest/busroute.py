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
        st =str(self._line_number) + " "  + self.origin + " " + self.destination + " " + str(self.list_stops) +" " + str(self._bus_schedule)
        return st



    def search_route(self, k,v) -> bool:
        current = False
        match(k):
            case 'origin':
                current = (self.origin == v)
            case 'destination':
                current = (self.destination == v)
            case 'stop':
                current =  (v in self.list_stops)
        if current:
            return True
        else:
            return False


    def get_dict(self):
        my_dict = {}
        my_dict['origin'] = self.origin
        my_dict['destination'] = self.destination
        my_dict['list_stops'] = self.list_stops
        my_dict['bus_schedule'] = {}
        for d in self._bus_schedule:
            print(d)
            print(self._bus_schedule)
            my_dict['bus_schedule'][d] = self._bus_schedule[d].get_dict_s()
        print (my_dict)
        return my_dict


    def display_r(self):
        print(self.__str__())
        for s in self._bus_schedule:
            print(self._bus_schedule[s])


    def update_route(self, origin:str, destination:str, list_stops:list):
        # for BusRoute[line_number]:
        self.origin = origin
        self.destination= destination
        self.list_stops = list_stops



    def add_schedule(self, origin_time:int, destination_time:int, driver_name:str):
        s = schedule.ScheduledRides(origin_time, destination_time, driver_name)
        id:int = int(random.randrange(1,1000))
        self._bus_schedule[id] = s

    # def add_delay(self, ):

    def get_sc_dict(self):
        print(self._bus_schedule)


a = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
c = BusRoute(7,'bal', 'rm', ['aaa','bbb'])
a.add_schedule(9,11,'noa')
a.get_dict()



# a.search_route('origin', 'telaviv')

# print(a)
# a.add_schedule(9,10,'noa')
# s.search('origin','telaviv')
