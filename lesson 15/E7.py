
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process

import datetime as datetime


def factorial(n):
    for i in range(500):
        factor = 1
        for i in range(1,n+1):
            factor *= i
        return(n, factor)

def display(c):
    print(f'{c.result()[0]}! = {c.result()[1]}')


if __name__ == '__main__':
    start = datetime.datetime.utcnow()
    futures = []
    with ProcessPoolExecutor(max_workers=8) as executer:
        for n in range(100000):
            futures.append(executer.submit(factorial,1550))
        for c in futures:
            c.add_done_callback(display)
    end = datetime.datetime.utcnow()
    print(end-start)

