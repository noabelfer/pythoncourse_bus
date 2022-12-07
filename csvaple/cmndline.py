#!/usr/bin/python

import sys
import csv

infile = sys.argv[1]

print(infile)

with open(infile, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  
    for i,row in enumerate(spamreader):
        if(i == 10):
            break;
        if(i == 0):
            header = row
            print(len(header),header)
            apledata = [[] for i in range(len(header))]
            print(apledata)
        else:
            for col in range(len(header)):
                apledata[col].append(row[col])
    
    for i in range(len(header)):
        print(apledata[i])
