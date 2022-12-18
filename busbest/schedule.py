from datetime import time
import random



class ScheduledRides:
    def __init__(self, _origin_time:str, _destination_time:str, _driver_name:str, _delays = None):
        self._iid = _iid
        self._origin_time = _origin_time
        self._destination_time = _destination_time
        self._driver_name = _driver_name
        self._delays:list = _delays

    def __str__(self):
        return f'id:{self._iid} \n origin_time:{self._origin_time} \n destination_time:{self._destination_time} '

    def __repr__(self):
        print('rere')
        return f'id:{self._iid} \n origin_time:{self._origin_time} \n destination_time:{self._destination_time}'

    def get_dict_s(self):
        s_dict = {}
        s_dict['origin_time'] = self._origin_time
        s_dict['destination_time'] = self._destination_time
        s_dict['delays'] = self._delays
        return s_dict


    def _add_delay(self, delay_min):
        self._delays.append(delay_min)

    def _get_origin(self)->str:
        return str(self._origin_time)



