from busbest import best_bus
import time
import datetime

class Bus:
    def __init__(self, company: best_bus.BestBusCompany):
        self._company: best_bus.BestBusCompany = company

    def _select(self, massage, low_option, high_option) -> int:
        print(massage)
        while True:
            a = input('select  ')
            if not a.isnumeric():
                print ('please enter a number:')
                continue
            b = int(a)
            if b < low_option or b > high_option:
                print(f'please enter a number between {low_option} {high_option}: ')
                continue
            return b

    def _top_menu(self) :
        men1 = self._select ("[1] for Manager type 1 \n[2] for Passenger type 2" ,1 ,2)
        if men1 == 1:
            if not self._password():
                return
            self._menu_manager()
        if men1 == 2:
            self._menu_passenger()


    def _password(self) -> bool:
        for i in range (0,3):
            p = input("please enter password here:  ")
            if p == "RideWithUs!":
                return True
        print('password is incorrect')
        return False


    def _menu_manager(self) -> int:
        while True:
            menu_man = self._select("[1] add_route \n[2] delete_route \n[3] update_route \n[4] add_schedule \n[5] company_info \n[6] quit", 1, 6)
            match(menu_man):
                case 1: self._add_route()
                case 2: self._delete_route()
                case 3: self._update_route()
                case 4: self._add_schedule()
                case 5: self._company_info()
                case 6: return


    def _add_route(self):
        line = self._select("please enter line number: ", 1, 1000)
        add = input("please type origin, destination and stops, comma seperated: ")
        add1 = add.split(',')
        if len(add1) < 3:
            print('wrong input')
            return
        stops = []
        for i in range(2, len(add1)):
            stops.append(add1[i])
        self._company._add_route(line, add1[0], add1[1], stops)

    def _delete_route(self):
        line_to_del = self._select("please type the line number you would like to delete: ", 1,1000)
        #checks if line number exists:
        if not self._company.is_line(line_to_del):
            print(f'the line number:{line_to_del} does not exist!')
        if self._company.is_line(line_to_del):
            q = input("are you sure you want to delete this route? type: y/n")
            if q != 'y':
                print('no line has been deleted!')
                return
            print(f'line {line_to_del} has been deleted!')
            self._company._delete_route(line_to_del)


    def _add_schedule(self):
        line_number = self._select("please select the line you would like to add schedule to: ", 1, 1000)
        if self._company.is_line(line_number):
            add_s = input("please add the origin time(format HH:MM), destination time (format HH:MM) and driver name, comma seperated: ")
            sch = add_s.split(',')
            if len(sch) != 3:
                return
            driver_name  = sch[2]
            origin_time = sch[0]
            destination_time = sch[1]
            print("the schedule has been added to the route!")
            self._company._display_route_by(line_number)._add_schedule(origin_time, destination_time, driver_name)


    def _update_route(self):
        line_to_update = self._select("please type the line number you would like to update: ", 1, 1000)
        #checks if line number exists:
        if not self._company.is_line(line_to_update):
            print(f'the line number:{line_to_update} does not exist!')
        if self._company.is_line(line_to_update):
            origin = input("please enter the origin")
            destination = input("please enter the destination")
            stops = input('please enter the list of stops, comma seperated')
            list_stops = []
            for s in range(0,len(stops)):
                list_stops.append(s)
            print("the route has been updated!")
            self._company._update_route(origin, destination, list_stops)

    #presents all the info on all routes and schedules:
    def _company_info(self):
        print(self._company._display_route())


    def _menu_passenger(self):
        menu_pas = self._select("[1] search_route \n [2] add_delay \n [3] quit", 1, 3)
        match (menu_pas):
            case 1: self._search_route()
            case 2: self._add_delay()
            case 3: self._top_menu()

    def _search_route(self):
        search_field = self._select("please select the field you would like to search by:\n [1] line_number \n [2] origin \n [3] destination \n [4] stops \n [5] quit", 1, 5)
        match (search_field):
            case 1:self._search_byline()
            case 2:self._search_origin()
            case 3:self._search_destination()
            case 4:self._search_bystops()
            case 5:return

    def _add_delay(self):
        line = self._select("please insert the line you would like to report the delay:", 1,1000)
        if not self._company.is_line(line):
            print(f'the line number:{line} does not exist!')
        if self._company.is_line(line):
            print(f'this is the information for line: {line}: ')
            print(self._company._display_route_by(line))
            id = int(input('enter the bus ride id from the list above: '))
            delay = int(input("please enter the number of minutes of the delay: "))
            print(f"thank you for adding delay for line number {line}, id: {id}!")
            return self._company._display_route_by(line)._add_delay(delay,id)



    def _search_origin(self):
        origin = input("please insert the origin would like to search: ")
        for l in self._company._search_origin(origin):
            print(self._company._display_route_by(l))
        print(f'origin {origin} not found')

    def _search_destination(self):
        destination = input("please insert the destination would like to search: ")
        for l in self._company._search_destination(destination):
            print(self._company._display_route_by(l))
        print(f'destination {destination} not found')

    def _search_byline(self):
        line_number = self._select("please insert the line you would like to search: ", 1,1000)
        if self._company.is_line(line_number):
            print(self._company._display_route_by(line_number))
        else: print('no such line number')

    def _search_bystops(self):
        station = input("please insert the station you would like to search by: ")
        for l in self._company._search_station(station):
            print(self._company._display_route_by(l))







