# Implement a function that receives a csv file_path (str), and returns the following:
# List of column names
# Number of rows in the file
# Number of columns in the file
# Notes:
# you can assume that the csv file is correct and is not corrupted
# Consider using DictReader
import os.path
import csv

def csv_1(file_path):
    if not os.path.exists(file_path):
        raise ValueError
    data = []
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    headers = (data[0])
    number_cols = len(data[0])
    number_rows = len(data)
    return number_rows


a = csv_1("/Users/noabelfer/Downloads/addresses.csv")
print(a)
