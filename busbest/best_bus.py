
import random

from busbest import busroute


class BestBusCompany:
    def __init__(self):
        self.__bus_route: {classmethod} = {}

    # #when adding schedule, returns bus route object:
    # def broute(self, line: int) -> busroute:
    #     return self.__bus_route[line]

    def present_sched(self, line_number):
        return self.__bus_route[line_number].present_sched()

    def display_c(self):
        return self.__bus_route

    def display_route_by(self, line_number):
        return self.__bus_route[line_number]

    #diaplays all company info
    def display_route(self):
        print(self.__bus_route)



    #adds object from type busroute (class) to bus_route dict:
    def add_route(self, line_number, origin, destination, list_stops) -> bool:
        if line_number in self.__bus_route:
            return False
        b = busroute.BusRoute(line_number, origin, destination, list_stops)
        self.__bus_route[line_number] = b
        return True

    def delete_route(self, line_number) -> bool:
        if not line_number in self.__bus_route:
            return  False
        if line_number in self.__bus_route:
                del self.__bus_route
                print(f'line {line_number} has been deleted')
        else:
            print('no such line number')
            return

    def update_route(self, origin, destination, list_stops: list):
        # for BusRoute[line_number]:
        self.origin = origin
        self.destination = destination
        self.list_stops = list_stops

    # searches for stations and returns list of lines that include this station:
    def search_station(self, station) -> list:
        stops_lst = []
        for line in self.__bus_route:
            if self.__bus_route[line].search_station(station):
                stops_lst.append(line)
        return stops_lst

    #searches for origin and returns list of lines that include this origin:
    def search_origin(self, origin) ->list:
        origin_lst = []
        for line in self.__bus_route:
            if self.__bus_route[line].search_origin(origin):
                origin_lst.append(line)
        return origin_lst

    # searches for destination and returns list of lines that include this destination:
    def search_destination(self, destination) ->list:
        dest_lst = []
        for line in self.__bus_route:
            if self.__bus_route[line].search_destination(destination):
                dest_lst.append(line)
        return dest_lst


    #checks if line exists in route:
    def is_line(self, line_number) -> bool:
        if line_number in self.__bus_route:
            return True
        else:
            return False

    def add_delay(self, delay_min, id):
        return self.__bus_route.add_delay(delay_min,id)
#
# company = BestBusCompany()
# company.add_route(4,'telaviv','raanana',['aaa','bbb'])

# company.add_route(6,'telaviv','raanana',['aah','jbb'])
# company.broute(4).add_schedule(9,10,"Moshe")
# # print(company.display_route_by(4))
# print(company.search_origin('telaviv'))

# company.display_route_by(4).add_schedule(12, 13 ,"Moshe")
# print(company.present_sched(4))
# company.broute(4).update_route('yy','bb',['mk','dr','se'])
# print(company.display_c())
# # company.search_items_val('origin', 'telaviv')












