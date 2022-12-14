import datetime
import pickle
import schedule
import busroute
import best_bus


class Bus:
    def __init__(self, company: best_bus.BestBusCompany):
        self._company: best_bus.BestBusCompany = company

    def select(self, massage, low_option, high_option) -> int:
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


    def top_menu(self) :
        men1 = self.select ("[1] for Manager type 1 \n[2] for Passenger type 2" ,1 ,2)

        if men1 == 1:
            if not self.password():
                return
            self.menu_manager()


        if men1 ==2:
            self.menu_passenger()





    def password(self) -> bool:
        for i in range (0,3):
            p = input("please enter password here:  ")
            if p == "3":
                return True
        print('password is incorrect')
        return False


    def menu_manager(self) -> int:
        while True:
            menu_man = self.select("[1] add_route \n[2] delete_route \n[3] update_route \n[4] add_schedule \n[5] company_info \n [6] quit", 1, 5)
            match(menu_man):
                case 1: self.add_route()
                case 2: self.delete_route()
                case 3: self.update_route()
                case 4: self.add_schedule()
                case 5: self.company_info()
                case 6: return


    def add_route(self):
        line = self.select("please enter line number: ", 1, 1000)
        add = input("please type origin, destination and stops, comma seperated: ")
        add1 = add.split(',')
        if len(add1) < 3:
            print('wrong input')
            return
        stops = []
        for i in range(2, len(add1)):
            stops.append(add1[i])
        self._company.add_route(line, add1[0], add1[1], stops)

    def delete_route(self):
        line_to_del = self.select("please type the line number you would like to delete: ", 1,1000)
        #checks if line number exists:
        if self._company.is_line(line_to_del):
            q = input("are you sure you want to delete this route? type: y/n")
            if q != 'y':
                print('no line has been deleted!')
                return
            self._company.delete_route(line_to_del)
            print(f'line {line_to_del} has been deleted!')

    def add_schedule(self):
        line_number = self.select("please select the line you would like to add schedule to: ", 1, 1000)
        if self._company.is_line(line_number):
            add_s = input("please add the origin time, destination time and driver name, comma seperated: ")
            if len(add_s) != 3:
                return
            sch = add_s.split(',')
            origin_time,  destination_time, driver_name  = sch[0], sch[1], sch[3]
            self._company.broute(line_number).add_schedule(origin_time,  destination_time, driver_name)

    def update_route(self):
        pass
        # line_to_update = self.select("please type the line number you would like to update: ", 1, 1000)
        # # checks if line number exists:
        # if self._company.is_line(line_to_update):


    def company_info(self):
        print(self._company.display_c())


    def menu_passenger(self):
        menu_pas = self.select("[1] search_route \n [2] add_delay", 1, 2)

    # def search_route:
    #     pass



if __name__ == '__main__':
    print('bhy')
    # company = best_bus.BestBusCompany()
    # b = Bus(company)
    # b.top_menu()
    # company.add_route(1,'gtv','nui','ijo')
    # company.broute(1).add_schedule(3,4,'noa')
    # company.display_c()


