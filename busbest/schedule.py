from datetime import datetime
import random


class ScheduledRides:
    def __init__(self, origin_time:int, destination_time:int, driver_name:str):
        self.id = id
        self.origin_time = origin_time
        self.destination_time = destination_time
        self.driver_name = driver_name
        self.delays:list = []


    def __str__(self):
        st = str(self.id) + "  " + str(self.origin_time) + " " + str(self.destination_time) + " " + str(self.driver_name)
        return st


    def get_dict_s(self):
        s_dict = {}
        s_dict['origin_time'] = self.origin_time
        s_dict['destination_time'] = self.destination_time
        s_dict['delays'] = self.delays
        return s_dict

    #
    def add_delay(self, delay_min):
        self.delays.append(delay_min)




