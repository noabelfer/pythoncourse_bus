# Implement a function csv2json().
# The function receives a file_path of csv
# file and file_path of a new json file that
# will be created by a function. The function should read
# x§the original csv file, convert the data in it into json,
# and store the contents of the csv file as a json file that
# contains a list of objects. For example, for this csv file
# the result should be like this json file

import csv
import json
def csv2json(file_path_csv, file_path_json):
    with open(file_path_csv,'r') as file:
        reader = csv.reader(file)
        data = [{k: v for k, v in row.items()} for row in reader]
    with open(file_path_json, "w") as f:
        json.dump(data,f)

