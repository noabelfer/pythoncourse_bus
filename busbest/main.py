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
            if a < low_option or a > high_option:
                print(f'please enter a number between {low_option} {high_option}: ')
                continue
            return int(a)


    def menu_1(self) -> int:
        men1 = self.select ("[1] for Manager type 1 \n [2] for Passenger type 2" ,1 ,2)

        if men1 == 1:
            self.password()
            self.menu_manger()



    def password(self):
        for i in range (0,3):
            p = input("please enter password here:  ")
            if p == "RideWithUs!":
                return
        print('password is incorrect')
        exit()

    def menu_manger(self):
        menu_man = self.select("[1] add_route \n [2] delete_route \n [3] update_route", 1, 3)

    def add_route(self):
        line = self.select("please enter line number: ", 1, 1000)
        add = input("please type origin, destination and stops comma seperated: ")
        add1 = add.split(',')
        if len(add1) < 3:
            print('wrong input')
            return
        stops = []
        for i in range(2, len(add1)):
            stops.append(add1[i])
        self.company.add_route(line, add1[0], add1[1], stops)


    def menu_passenger(self):
        menu_pas = self.select("[1] search_route \n [2] add_delay", 1, 2)


    if __name__ == '__main__':

        menu_1()
        if select ==

