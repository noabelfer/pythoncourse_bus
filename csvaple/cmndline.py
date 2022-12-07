#!/usr/bin/python

import sys
import csv

#infile = sys.argv[1]
infile = "AAPL.csv"

print(infile)
LOW_COL = 1
HIGH_COL = 4
VOLUME_COL = 3
with open(infile, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    pre_year = 0
    dict = {}
    for i,row in enumerate(spamreader):
        if(i == 0):
            header = row
            print(len(header),header)
        else:
            #Date,Low,Open,Volume,High,Close,Adjusted Close
            # 0     1   2     3     4    5       6
            year = row[0].split('-')[2]
            if(year != pre_year):
                dict[year] = {'lowpriice':  [],'highprice':[],'volume':[]}
                pre_year = year
            dict[year]['lowpriice'].append(float(row[LOW_COL]))
            dict[year]['highprice'].append(float(row[HIGH_COL]))
            dict[year]['volume'].append(float(row[VOLUME_COL]))

    for y in dict.keys():
        low_price  = min(dict[y]['lowpriice'])
        high_price = max(dict[y]['highprice'])
        ave_volume = sum(dict[y]['highprice'])/len(dict[y]['highprice'])
        min_volume = min(dict[y]['highprice'])
        max_volume = max(dict[y]['highprice'])
        print('year: ',y,' low_p: ',low_price,' high_p: ',high_price,' ave_vol: ',ave_volume,' min_vol: ',min_volume,' max_vol: ',max_volume)
        
  
 #   print(dict)
