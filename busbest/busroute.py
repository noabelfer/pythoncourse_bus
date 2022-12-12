import random

from busbest import schedule


class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, list_stops: list):
        self.my_dict = {}
        self.my_dict['origin'] = origin
        self.my_dict['destination'] = destination
        self.my_dict['list_stops'] = list_stops
        self._bus_schedule = {}
        self._line_number: int = line_number


    def __str__(self) -> str:
        st =str(self._line_number) + " "  + self.my_dict['origin'] + " " + self.my_dict['destination'] + " " + str(self.my_dict['list_stops']) +" " + str(self._bus_schedule)
        return st
        #return str(self.line_number + " " + self.origin + " " + self.destination + " " + str(self.list_stops) )

    def search(self, k,v):
        for d in self.my_dict:
            if d == k and self.my_dict[k] == v:
                self.my_dict.get(k)
                print(self.my_dict, self._bus_schedule)
                # my_dict_copy = self.my_dict
                # my_dict_copy['schedule'] = self.st
                # return my_dict_copy
            else:
                return {}


    def display_r(self):
        print(self.__str__())
        for s in self._bus_schedule:
            print(self._bus_schedule[s])


    def update_route(self, origin:str, destination:str, list_stops:list):
        # for BusRoute[line_number]:
        self.my_dict['origin'] = origin
        self.my_dict['destination']= destination
        self.my_dict['list_stops'] = list_stops



    def add_schedule(self, origin_time:int, destination_time:int, driver_name:str):
        s = schedule.ScheduledRides(origin_time, destination_time, driver_name)
        id:int = int(random.randrange(1,1000))
        print(id)
        self._bus_schedule[id] = s



a = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
c = BusRoute(7,'bal', 'rm', ['aaa','bbb'])
c.search('origin','bal')
a.search('origin','telaviv')
a.add_schedule(9,11,'noa')

print(a)
# a.add_schedule(9,10,'noa')
# s.search('origin','telaviv')
