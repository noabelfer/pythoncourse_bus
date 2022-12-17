import os
import time
import datetime
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

    print("=====Hello and welcome to BestBusCompany!=====")
    b = menu.Bus(company)
    b._top_menu()


    file = open('company.pickle', 'wb')
    pickle.dump(company, file)
