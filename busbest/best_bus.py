from busbest import busroute
import random


class BestBusCompany:
    def __init__(self):
        self.__bus_schedule = None
        self.__bus_route: {classmethod} = {}

    def display_c(self):
        for bus in self.__bus_route:
            self.__bus_route[bus].display_r()

    #adds object from type busroute (class) to bus_route dict:
    def add_route(self, line_number, origin, destination, list_stops) -> bool:
        if line_number in self.__bus_route:
            return False
        b = busroute.BusRoute(line_number, origin, destination, list_stops)
        self.__bus_route[line_number] = b
        return True

    def delete_route(self, line_number):
        if line_number in self.__bus_route.keys():
            q = input("are you sure you want to delete this route? type: y/n")
            if q == 'y':
                self.__bus_route.pop(line_number)
        print('no such line number')
        return



    #adds object from type bus schedule {} (class) to self. bus_route class
    # def add_schedule(self,line_number:int, origin_time:int, destination_time:int, driver_name:str):
    #     self.__bus_route[line_number].add_schedule(origin_time , destination_time, driver_name)



company = BestBusCompany()
company.add_route(4,'telaviv','raanana',['aaa','bbb'])
company.add_schedule(4,9,10,'moshe')
company.display_c()
company.













