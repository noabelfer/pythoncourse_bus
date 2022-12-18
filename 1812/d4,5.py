import datetime
#
# Implement a function that gets a dictionary of the format below
# and returns it's elements sorted first by status (great - good - bad),' \
#               ' then by total minutes late, then by name.


# (3,130, jacob)

def minutes(hour:str) -> float:
    minutes : datetime.timedelta = datetime.datetime.strptime(hour, "%Hh %Mm") - \
                                    datetime.datetime(year = 1900, month = 1, day = 1)
    return(minutes.total_seconds() // 60)

def status(status:str) ->int:
    return len(status)

def func(bus_dict:dict) -> tuple:
    s = status(bus_dict["status"])
    name = bus_dict["name"]
    time_sum = 0
    for t in bus_dict["delays"]:
        time_sum += minutes(t)
    return(s,time_sum,name)








buses = [
        {
           "delays": ['1h 20m', '25m', '3h', '2h 1m'],
           "status": 'bad',
           "name": "Jacob",
           "route_num": 560
        },
       {
           "delays": ['20m', '5m', '3h'],
           "status": 'great',
           "name": "Moshe",
           "route_num": 769
        },
       {
           "delays": ['2h 3m'],
           "status": 'good',
           "name": "Jack",
           "route_num": 766
        },
       {
           "delays": ['6h'],
           "status": 'great',
           "name": "Mark",
           "route_num": 876
        },
         {
           "delays": ['2h 3m'],
           "status": 'good',
           "name": "Anna",
           "route_num": 456
        },
]



print(sorted(buses, key = func))