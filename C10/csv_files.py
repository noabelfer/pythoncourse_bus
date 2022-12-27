import os
import pathlib
import csv
from C10.text import TextFile


class Csv(TextFile):
    def __init__(self, path):
        super().__init__(path)
        if not self._file_exist:
            raise Exception(f"file {path} does not exist")
        if self._type != "csv":
            raise Exception ("file is not csv")

    def get_content(self) -> str:
        self._open()
        dict = {}
        list_dicts = []
        rcsv = csv.DictReader(self._file_handle)
        for k, v in enumerate(rcsv):
            dict[k] = v
            list_dicts.append(dict[k])
        self._file_handle.close()
        # print(list_dicts)
        return list_dicts

    def get_rows_num(self) -> int:
        d = self.get_content()
        return len(d)

    def get_columns_num(self) -> int:
        d = self.get_content()
        return len(d[0])

    def get_row(self, row_num):
        d = self.get_content()
        if row_num > len(d):
            raise Exception("row num is out of range")
        else:
            row = d[row_num-1]
            return row

    def get_column(self, column_num):
        dict = self.get_content()
        for i in range(0,len(dict[0])):
            return dict[i][column_num]

    def __add__(self, toadd):
        fname = self._dir_path + '/' + self.basename + '_' + toadd.basename + '.csv'
        content = self.get_content()
        content1 = toadd.get_content()
        content += content1
        # if os.path.exists(fname):
        #     raise Exception(f'File {fname} exists!')

        with open(fname, mode='w', newline='') as csv_file:
            keysList = content[0].keys()
            w = csv.DictWriter(csv_file, fieldnames=keysList)
            w.writeheader()
            for dict in content:
                w.writerow(dict)
        csv_file.close()
        added = Csv(fname)
        return added



a = Csv("/Users/noabelfer/Downloads/AAPL.csv")
b = Csv("/Users/noabelfer/Downloads/AAPL.csv")
c = (a+b)
# print(a.get_columns_num())
# print(a.get_row(3))
# print(a.get_content())
# print(a.get_rows_num())

