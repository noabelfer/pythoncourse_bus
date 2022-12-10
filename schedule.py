from datetime import datetime


class ScheduledRides:
    def __init__(self, origin_time:int, destination_time:int, driver_name:str):

        self.id = id
        self.origin_time = origin_time
        self.destination_time = destination_time
        self.driver_name = driver_name
        self.delays = []

    def __str__(self):
        st = str(self.id) + "  " + str(self.origin_time) + " " + str(self.destination_time) + " " + self.driver_name
        return st

