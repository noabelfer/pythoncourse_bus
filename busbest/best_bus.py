
import random

from busbest import busroute


class BestBusCompany:
    def __init__(self):
        self._bus_route: {classmethod} = {}

    def _present_sched(self, line_number):
        return self._bus_route[line_number]._present_sched()

    def _display_c(self):
        return self._bus_route

    def _display_route_by(self, line_number):
        return self._bus_route[line_number]

    #diaplays all company info
    def _display_route(self):
        print(self._bus_route)

    #adds object from type busroute (class) to bus_route dict:
    def _add_route(self, line_number, origin, destination, list_stops) -> bool:
        if line_number in self._bus_route:
            return False
        b = busroute.BusRoute(line_number, origin, destination, list_stops)
        self._bus_route[line_number] = b
        return True

    def _delete_route(self, line_number) -> bool:
        if not line_number in self._bus_route:
            return False
        if line_number in self._bus_route:
                del self._bus_route
                print(f'line {line_number} has been deleted')
        else:
            print('no such line number')
            return

    def _update_route(self, origin, destination, list_stops: list):
        # for BusRoute[line_number]:
        self._origin = origin
        self._destination = destination
        self._list_stops = list_stops

    # searches for stations and returns list of lines that include this station:
    def _search_station(self, station) -> list:
        stops_lst = []
        for line in self._bus_route:
            if self._bus_route[line].search_station(station):
                stops_lst.append(line)
        return stops_lst

    #searches for origin and returns list of lines that include this origin:
    def _search_origin(self, origin) ->list:
        origin_lst = []
        for line in self._bus_route:
            if self._bus_route[line]._search_origin(origin):
                origin_lst.append(line)
        return origin_lst

    # searches for destination and returns list of lines that include this destination:
    def _search_destination(self, destination) ->list:
        dest_lst = []
        for line in self._bus_route:
            if self._bus_route[line].search_destination(destination):
                dest_lst.append(line)
        return dest_lst


    #checks if line exists in route:
    def is_line(self, line_number) -> bool:
        if line_number in self._bus_route:
            return True
        else:
            return False

    def _add_delay(self, delay_min, id):
        return self._bus_route._add_delay(delay_min,id)
#
# company = BestBusCompany()
# company._add_route(4,'telaviv','raanana',['aaa','bbb'])
# #
# # company._add_route(6,'telaviv','raanana',['aah','jbb'])
# company._display_route_by(4)._add_schedule(9,10,"Moshe")
# # print(company._display_route_by(4))
# # print(company._search_origin('telaviv'))
# print(company._present_sched(4))
# company._bus_route._add_schedule(12, 13 ,"Moshe")
# print(company._present_sched(4))
# company.broute(4).update_route('yy','bb',['mk','dr','se'])
# print(company.display_c())
# # company.search_items_val('origin', 'telaviv')












