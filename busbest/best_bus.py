
import random

from busbest import busroute


class BestBusCompany:
    def __init__(self):
        self.__bus_route: {classmethod} = {}

    #when adding schedule, returns bus route object:
    def broute(self, line: int) -> busroute:
        return self.__bus_route[line]

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

    def search_items_val(self, search_item_key, search_item_val):
        for l in self.__bus_route.keys():
            s = self.__bus_route[l]
            dict =  s.search(search_item_key, search_item_val)
            if s.search_item_key == self.__bus_route[search_item_key]:
                print(s.search)
                return self.search_items_val()

    def search_line(self, k, v):
        for l in self.__bus_route:
            a = self.__bus_route[l].search(k,v)



    #adds object from type bus schedule {} (class) to self. bus_route class
    # def add_schedule(self,line_number:int, origin_time:int, destination_time:int, driver_name:str):
    #     self.__bus_route[line_number].add_schedule(origin_time , destination_time, driver_name)


company = BestBusCompany()
company.add_route(4,'telaviv','raanana',['aaa','bbb'])
company.add_route(6,'telaviv','raanana',['aah','jbb'])


company.broute(4).add_schedule(9,10,"Moshe")
company.broute(4).update_route('yy','bb',['mk','dr','se'])
company.display_c()
company.search_items_val('origin', 'telaviv')












