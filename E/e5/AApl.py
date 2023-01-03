import csv
import os
import statistics
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


class Csvmanage:
    def __init__(self, path):
        self.data = None
        self._path = path
        self._file_exist:bool = os.path.exists(path)
        # self.row_dict = None
        if self._file_exist is False:
            raise ValueError(f'file {path} does not exist')


    def data_create(self):
        with open(self._path, 'r') as file:
            reader = csv.DictReader(file)
            data = {}
            for row in reader:
                date = row['Date']
                date_obj = datetime.strptime(date, '%d-%m-%Y')
                year = date_obj.year
                if year not in data:
                    data[year] = []
                data[year].append(row)
        for year, rows in data.items():
            with open(f'AAPL_{year}.csv', 'w') as file:
                print(reader.fieldnames)
                writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                writer.writeheader()

                avg = {}
                #opens a new blank row
                for keys in reader.fieldnames:
                    avg[keys] = float(0)
                #adds the sums of objects to the avg row
                for apple_row in data[year]:
                    writer.writerow(apple_row)
                    for keys in range(1,len(reader.fieldnames)):
                        avg[reader.fieldnames[keys]] += float(apple_row[reader.fieldnames[keys]])

                for keys in reader.fieldnames:
                    avg[keys] /= len(data[year])
                writer.writerow(avg)
                file.close()


            # with open(f'AAPL_{year}.csv', "r") as f:
            #     reader = csv.reader(f)
            #     next(reader)





            # for data[year]:


        #         sum_data = {key: 0 for key in reader.fieldnames}
        #         count = 0
        #         for row in rows:
        #             # Write the row to the CSV file
        #             writer.writerow(row)
        #             for key in sum_data:
        #                 sum_data[key] += (row[key])
        #             count += 1
        #         # Calculate the averages for each column
        #         averages = {key: sum_data[key] / count for key in sum_data}
        #
        #         # Add the averages to the dictionary and write it to the CSV file
        #         row = {**averages, 'date': f'{year} averages'}
        #         writer.writerow(row)
    #     file.close()
    #     return data
    #
    # def write_file(self):
    #     for line in open_file.data:
    #         if data[]



a = Csvmanage("/Users/noabelfer/Downloads/AAPL.csv")
a.data_create()
a.avg()
a.add_avg()