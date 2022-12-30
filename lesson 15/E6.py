#1
# Write a program that receives a number of seconds from
# a user and counts down this amount of seconds in
# resolution of 0.1 second by printing the amount of time left.
# For example, if the user inserts 3, your program should constantly print:
# 3 seconds left
# 2.9 seconds left
# 2.8 seconds left
# 2.7 seconds left
# ….
# 0.1 seconds left
# DONE!

import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures._base import Future

import requests


# def sec_left(n):
#     while n >= 0:
#         n -= 0.1
#         print(f'{round(n,1)} seconds left')
#     time.sleep(0.1)
#
# a=sec_left(3)


#2
def get_quote():
    print(f"Getting quote num")
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        print(response.json()['quote'])

    else:
        raise Exception(f"Received response code {response.status_code} for quote num")

def sec_left(n):
    with ThreadPoolExecutor() as a:
        while n >= 0:
            time.sleep(0.1)
            n -= 0.1
            print(f'{round(n,1)} seconds left')
            if round(n,1) - int(n) == 0:
                a.submit(get_quote)

    print("done")


a=sec_left(10)
