
import menu
from busbest import best_bus

if __name__ == '__main__':

    company = best_bus.BestBusCompany()
    b = menu.Bus(company)
    b.top_menu()
    # company.add_route(1,'gtv','nui','ijo')
    # company.broute(1).add_schedule(3,4,'noa')
    # company.display_c()


