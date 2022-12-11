import csv
import json
import os
from abc import abstractmethod, ABC


class Text_file(ABC):
    def __init__(self, file_path:str):
        #check path exists
        #check file type
        # store the path
        if not os.path.exists(file_path):
            raise Exception
        if os.path.splitext(file_path)[-1][1:] != self._get_ext():
            raise Exception
        self._file_path = file_path


    def get_file_size(self):
        pass


    def _get_content(self):
        with open(self._file_path, 'r') as fh:
            content = self.get_specific_content(fh)
        return content
        #open a file (fd / fh) - common for all
        #get content = specific

    @abstractmethod
    def get_specific_content(self, fh):
        pass


    # @abstractmethod
    # def is_extension_valid(self) -> bool :
    #     return self._file_path
    @abstractmethod
    def _get_ext(self):
        pass


class CsvFile(Text_file):
    def _get_ext(self):
        return 'csv'

    def get_specific_content(self, fh):
        ret_val = []
        for row in csv.DictReader(fh, delimeter = self._delimeter):
            ret_val.append(row)
        return ret_val


class TxtFile(Text_file):
    def __init__(self, file_path, delimeter=','):
        super().__init__(file_path)
        self._delimeter = delimeter

    def _get_specific_content(self, fh):
        return fh.read()

    def _get_ext(self):
        return 'txt'



class JsonFile(Text_file):
    def _get_specific_content(self, fh):
        return json.load(fh)

    def _get_ext(self):
        return 'json'


csv_file =CsvFile("/Users/noabelfer/PycharmProjects/pythoncourse/csvaple/AAPL.csv")
files_list = [csv_file]
for f in files_list:
    print(f.get_content())