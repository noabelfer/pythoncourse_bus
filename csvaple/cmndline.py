#!/usr/bin/python

import sys
import csv

#infile = sys.argv[1]
infile = "AAPL.csv"

print(infile)
LOW_PRICE_COL = 1
HIGH_PRICE_COL = 4
VOLUME_COL = 3
with open(infile, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    pre_year = 0
    dict = {}
    #Loop of reading all lines of csv file
    for i,row in enumerate(spamreader):
        #if first row just skip ,no data
        if(i == 0):
            header = row
            print(len(header),header)
        else:
            #Date,Low,Open,Volume,High,Close,Adjusted Close
            # 0     1   2     3     4    5       6
            #Extracting the year from column 0
            year = row[0].split('-')[2]
            # Here we check if the year has changed 
            if(year != pre_year):
                # adding year entry to data dictionay 
                dict[year] = {'lowpriice':  [],'highprice':[],'volume':[]}
                pre_year = year
            #appending data to year entry
            dict[year]['lowpriice'].append(float(row[LOW_PRICE_COL]))
            dict[year]['highprice'].append(float(row[HIGH_PRICE_COL]))
            dict[year]['volume'].append(float(row[VOLUME_COL]))
    #Here after reading all csv file  we do final computations on the lists
    for y in dict.keys():
        low_price  = min(dict[y]['lowpriice'])
        high_price = max(dict[y]['highprice'])
        ave_volume = sum(dict[y]['highprice'])/len(dict[y]['highprice'])
        min_volume = min(dict[y]['highprice'])
        max_volume = max(dict[y]['highprice'])
        print('year: ',y,' low_p: ',low_price,' high_p: ',high_price,' ave_vol: ',ave_volume,' min_vol: ',min_volume,' max_vol: ',max_volume)
        
  
 #   print(dict)
