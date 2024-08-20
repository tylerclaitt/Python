import pandas as pd
import csv
import os

projName = 'Aspire Health Partners-OSC Bridge Housing:ES'
# open file in read mode
with open('reference.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        if projName == row[2]:
            hmisID = row[3]
            projType = row[4]
            break
        print(row)
        
print(hmisID)
print(projType)
print(row[2])