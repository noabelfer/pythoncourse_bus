import concurrent
import csv
import os
import statistics
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


class Csvmanage:
    def __init__(self, path):
        self._data_dict_years = {}
        self._path = path
        self._file_exist:bool = os.path.exists(path)
        # self.row_dict = None
        if self._file_exist is False:
            raise ValueError(f'file {path} does not exist')

        with open(self._path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                    date = row['Date']
                    date_obj = datetime.strptime(date, '%d-%m-%Y')
                    year = date_obj.year
                    if year not in self._data_dict_years:
                        self._data_dict_years[year] = []
                    self._data_dict_years[year].append(row)
        file.close()

    def create_year_file(self, year):
        try:
            print('start year'+ str(year))
            fld_names = list(self._data_dict_years[year][0].keys())
            # print(fld_names)
            with open(f'AAPL_{year}.csv', 'w') as file:
                writer = csv.DictWriter(file, fieldnames = fld_names)
                writer.writeheader()
                avg = {}
                # opens a new blank row
                for key in fld_names:
                    avg[key] = float(0)
                 # adds the sums of objects to the avg row
                for apple_row in self._data_dict_years[year]:
                    writer.writerow(apple_row)
                for i in range(1, len(fld_names)):
                    avg[writer.fieldnames[i]] += float(apple_row[writer.fieldnames[i]])
                for key in fld_names:
                    avg[key] /= len(self._data_dict_years[year])
                writer.writerow(avg)
                file.close()
            print('end year' + str(year))
            return year
        except Exception as e:
            return str(year)+'  '+str(e)

    def run_as_threads(self):
        futures = []
        with ThreadPoolExecutor(max_workers=4) as executer:
            for year in range(list(self._data_dict_years.keys())[0], list(self._data_dict_years.keys())[-1]+1):
                futures.append(executer.submit(self.create_year_file,year))
            executer.shutdown()
        for f in concurrent.futures.as_completed(futures):
            print(f.result())





if __name__ == '__main__':
    a = Csvmanage("data/AAPL.csv")
    # a.create_year_file(1980)
    a.run_as_threads()
