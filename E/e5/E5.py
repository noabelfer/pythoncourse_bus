# import csv
#
# with open('/Users/noabelfer/Downloads/AAPL.csv', 'r') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     pre_year = 0
#     dict = {}
#     for i,row in enumerate(spamreader):
#         #if first row just skip ,no data
#         if(i == 0):
#             header = row
#             print(len(header),header)
#         else:
#             # Extracting the year from column 0
#             year = row[0].split('-')[2]
#             # Here we check if the year has changed
#             if (year != pre_year):
#                 with open(f'AAPL_{year}.csv', mode='w', newline='') as csvfile:
#                     w = csv.writer(f'AAPL_{year}.csv')
#                     writer.writerow(next(csv.DictReader(csvfile)))
#
#
import csv
import os
import pathlib
from datetime import datetime
import concurrent.futures


class Csvmanage:
    def __init__(self, csvpath: str):
        self.__exist: bool = os.path.exists(csvpath)
        self.__csvpath = csvpath
        if (not self.__exist):
            raise ValueError(f' file {csvpath} not exist!')
        self._suffix: str = pathlib.Path(csvpath).suffix
        self.__filename = os.path.basename(csvpath)
        self._dir_path: str = self.__csvpath.replace(self.__filename, '')
        self.__filename = self.__filename.replace(".csv", "")
        with open(csvpath, 'r') as f:
            rcsv = csv.DictReader(f)
            self.__csvdict = {}
            self.__years = {}
            curr_year = 0
            n = 0
            start_year = 0
            # loop of constructing 2 dictionaries:
            # 1. The csv is constructed in self.__csvdict[]
            # 2. self.__years contains a tuple for each year which includes
            #     {'year': (start_year,n)}
            #  start_year: is reference to self.__csvdict[] where the data for this year startswith
            #  n : bumber of rows for this year
            #  in our example:
            #    {1980: (0, 13), 1981: (13, 253), 1982: (266, 253), ...  2022: (10352, 19)}
            for k, v in enumerate(rcsv):
                self.__csvdict[k] = v
                date = datetime.strptime(v['Date'], "%d-%m-%Y")
                # For first row to avoid false detection of year change
                if (curr_year == 0):
                    curr_year = date.year
                # here we detect year change
                if (date.year != curr_year):
                    self.__years[curr_year] = (start_year, n)
                    curr_year = date.year
                    start_year = k
                    n = 0
                n += 1
            self.__years[curr_year] = (start_year, n)
            print(self.__years)
            print(self.__csvdict[0])
            f.close()

    def create_year_file(self, year: int):
        path = self._dir_path + self.__filename + '_' + str(year) + '.csv'
        start_row = self.__years[year][0]
        n_rows = self.__years[year][1]
        print(
            "started " + str(year) + "start key: " + str(start_row) + " len: " + str(n_rows) + " create file: " + path)
        fh = open(path, "w", newline='')
        keysList = [key for key in self.__csvdict[0].keys()]
        w = csv.DictWriter(fh, fieldnames=keysList)
        w.writeheader()
        average_line = {}
        for c in range(len(keysList)):
            average_line[keysList[c]] = float(0)
        average_line[keysList[0]] = 'Average'
        for l in range(start_row, start_row + n_rows):
            w.writerow(self.__csvdict[l])
            for c in range(1, len(keysList)):
                average_line[keysList[c]] += float(self.__csvdict[l][keysList[c]])

        for c in range(1, len(keysList)):
            average_line[keysList[c]] /= n_rows
        w.writerow(average_line)
        fh.close()
        print("ended " + str(year) + " create file: " + path)
        return year

    def run_as_threads(self):
        first_year = list(self.__years.keys())[0]
        last_year = list(self.__years.keys())[-1]
        print('first_year ' + str(first_year) + ' last_year ' + str(last_year))
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            results = [executor.submit(self.create_year_file, i) for i in range(first_year, last_year + 1)]

        executor.shutdown()
        for f in concurrent.futures.as_completed(results):
            print(f.result())


if __name__ == '__main__':
    a = Csvmanage("/Users/noabelfer/Downloads/pythonfiles/AAPL.csv")
    #  a.create_year_file(1983)
    a.run_as_threads()