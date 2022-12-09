import os
import sys
import csv

def search_csv_files(path):
    for (root, dirs, files) in os.walk(path):
        for f in files:
            if f.endswith(".csv"):
                fname = os.path.join(root, f)
                with open(fname, newline='') as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    for row in csvreader:
                        row_count = sum(1 for row in csvreader) 
                        fname_cols = len(row)
                        print('File :',fname,' lines: ',row_count,' cols ',fname_cols)
                        csvfile.close()
                        break

       
search_csv_files("..")
