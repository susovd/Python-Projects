#import required modules
import os
import csv

#define csv file path
csvpath = os.path.join('Resources', 'budget_data.csv')  #no need for .. as both the python file and Resources folder are in same folder

#open file, specify file type, i.e. delimeter
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader) #specify first row has header and ask to skip first row 

#declare variables and start counters
    numMonths = 0
    currentRevenue = 0
    lastRevenue = 0
    changeInRevenue = 0
    totalRevenueChange = 0
    maximumRevenueChange = 0
    minimumRevenueChange = 0
    totalRevenue = 0

#loop through each row to find values we need
    for eachRow in csvreader:
        numMonths = numMonths + 1 
        currentRevenue = eachRow[1] #diff
        totalRevenue = totalRevenue + int(currentRevenue) #diff
        changeInRevenue = int(currentRevenue) - int(lastRevenue)
        totalRevenueChange = totalRevenueChange + changeInRevenue 
        lastRevenue = eachRow[1]

        #find maximum change, assign first value as maximum value, Swap values if a bigger value comes in
        if changeInRevenue > maximumRevenueChange:
            maximumRevenueChange = changeInRevenue
            maximumRevenueChangeMonth = eachRow[0]
    
        #find minimum change, same logic as maximum valur but assign first value as minimum to start with
        if changeInRevenue < minimumRevenueChange:
            minimumRevenueChange = changeInRevenue
            minimumRevenueChangeMonth = eachRow[0]

    averageRevenueChange = totalRevenueChange / numMonths

# Q/N: In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#print results first
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {numMonths}")
print(f"Total: ${totalRevenue}")
print(f"Average Change: ${averageRevenueChange}")
print(f"Greatest Increase in Profits: {maximumRevenueChangeMonth} (${maximumRevenueChange})")
print(f"Greatest Decrease in Profits: {minimumRevenueChangeMonth} (${minimumRevenueChange})")

#write files into analysis folder, specify path, we are storing results in result.csv file inside analysis folder. 
#analysis folder and this python script are on same folder
output_path = os.path.join('analysis', 'results.txt')

#open file using write mode
with open(output_path, 'w') as txtfile:

    #initialize txt writer
    txtwriter = txt.writer(txtfile, delimiter = '')

    txtwriter.writerow(print("Financial Analysis"))