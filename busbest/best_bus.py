
import random

from busbest import busroute


class BestBusCompany:
    def __init__(self):
        self.__bus_route: {classmethod} = {}

    #when adding schedule, returns bus route object:
    def broute(self, line: int) -> busroute:
        return self.__bus_route[line]

    def display_c(self):
        return self.__bus_route
        # print(self.__bus_route[line_number])
        # print(self.__bus_route.get_schedule(line_number))

    def display_route(self):
        print(self.__bus_route)

        # for bus in self.__bus_route:
        #     print(self.__bus_route[bus].get_schedule())

            # self.__bus_route[bus].display_r()

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

    def search_items_val(self, line_number):
        for line_number in self.__bus_route:
            s = self.__bus_route[l]
            dict =  s.search(item_field, item_val)
            if s.search_item_key == self.__bus_route[item_field]:
                print(s.search)
                return self.search_items_val()

    # def search_line(self, k, v):
    #     for l in self.__bus_route:
    #         a = self.__bus_route[l].search(k,v)

    # def search_line(self, line_number):


    #checks if line exists
    def is_line(self, line_number) -> bool:
        if line_number in self.__bus_route:
            return True
        else:
            return False


    #adds object from type bus schedule {} (class) to self. bus_route class
    # def add_schedule(self,line_number:int, origin_time:int, destination_time:int, driver_name:str):
    #     self.__bus_route[line_number].add_schedule(origin_time , destination_time, driver_name)


# company = BestBusCompany()
# company.add_route(4,'telaviv','raanana',['aaa','bbb'])
# company.add_route(6,'telaviv','raanana',['aah','jbb'])
# company.delete_route(6)

# company.broute(4).add_schedule(9,10,"Moshe")
# company.broute(4).update_route('yy','bb',['mk','dr','se'])
# company.display_c(4)
# # company.search_items_val('origin', 'telaviv')












