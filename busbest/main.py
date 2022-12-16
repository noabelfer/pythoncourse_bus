import os

import menu
from busbest import best_bus
import pickle

if __name__ == '__main__':

    if not os.path.exists('company.pickle'):
        company = best_bus.BestBusCompany()
    else:
        # this is not the first time - we already have a DB
        # with data from the previous runs
        with open('company.pickle', 'rb') as fh:
            company = pickle.load(fh)


    b = menu.Bus(company)
    b.top_menu()
    # company.add_route(1,'gtv','nui','ijo')
    # company.broute(1).add_schedule(3,4,'noa')
    # company.display_c()


    file = open('company.pickle', 'wb')
    pickle.dump(company, file)
