from datetime import datetime
import random


class ScheduledRides:
    def __init__(self, origin_time:int, destination_time:int, driver_name:str, delays = None):
        self.id = id
        self.origin_time = origin_time
        self.destination_time = destination_time
        self.driver_name = driver_name
        self.delays:list = delays

    def __str__(self):
        return f'id:{self.id} origin_time:{self.origin_time} destination_time:{self.destination_time} driver name:{self.driver_name}'

    def __repr__(self):
        return self.__str__()

    def get_dict_s(self):
        s_dict = {}
        s_dict['origin_time'] = self.origin_time
        s_dict['destination_time'] = self.destination_time
        s_dict['delays'] = self.delays
        return s_dict

    #
    def add_delay(self, delay_min):
        self.delays.append(delay_min)




