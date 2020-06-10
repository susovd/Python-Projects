#import required modules
import os
import csv

#define csv file path
csvpath = os.path.join('Resources', 'election_data.csv')  #no need for .. as both the python file and Resources folder are in same folder

#open file, specify file type, i.e. delimeter
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader) #specify first row has header and ask to skip first row 

#declare and initialize variables
    totalVotes = 0


    for eachRow in csvreader:
        totalVotes = totalVotes + 1



print(f"Total votes cast: {totalVotes}")