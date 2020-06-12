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

#I filtered the csv files and found there are 4 candidates. So, the plan is to assign each candidate an empty list and append each vote to respective using conditionals. 
# Length of the each list candidate list will give number of votes.
#candidate are Khan, Correy, O'Tooley and Li
#summing each row will give number of votes

    votes = []
    candidates = []
    Khan = []
    Li = []
    Correy = []
    Tooley = []


    
#create separate list for voters and candidates and add to the list with each iteration
    for eachRow in csvreader:
        votes.append(eachRow[0])
        candidates.append(eachRow[2])

    for candidate in candidates:
        if candidate == "Khan":
            Khan.append(candidate)
        elif candidate == "Li":
            Li.append(candidate)
        elif candidate == "Correy":
            Correy.append(candidate)
        else:
            Tooley.append(candidate)

#calculate numbers
numKhanVotes = len(Khan)
numLiVotes = len(Li)
numCorreyVotes = len(Correy)
numTooleyVotes = len(Tooley)
totalVotes = len(votes)

maxvotes = "Khan"

if numKhanVotes < numCorreyVotes:
    maxvotes = "Correy"  

if numKhanVotes < numLiVotes:
    maxvotes = "Li"

if numKhanVotes < numTooleyVotes:
    maxvotes = "O'Tooley"

#create a dictionary of votes for each candidate
#voteCountDict = {
 #   "Khan" : numKhanVotes,
  #  "Li": numLiVotes,
   # "Correy" :numCorreyVotes,
    #"O'Tooley": numTooleyVotes
#}
#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

#winner = max(voteCountDict, key = lambda k:voteCountDict[k]) 

winner = maxvotes
KhanPct = (numKhanVotes/totalVotes) *100
LiPct = (numLiVotes/totalVotes) *100
CorreyPct = (numCorreyVotes/totalVotes) *100
TooleyPct = (numTooleyVotes/totalVotes) * 100

#formatting output as requested in question
KhanPct_format = format(KhanPct, '.3f')
LiPct_format = format(LiPct, '.3f')
CorreyPct_format = format(CorreyPct, '.3f')
TooleyPct_format = format(TooleyPct, '.3f')

print("Election Results")
print("---------------------------")
print(f"Total Votes:{totalVotes} ")
print("---------------------------")
print(f"Khan: {KhanPct_format}% ({numKhanVotes}) ")
print(f"Correy: {CorreyPct_format}% ({numCorreyVotes}) ")
print(f"Li: {LiPct_format}% ({numLiVotes}) ")
print(f"Tooley: {TooleyPct_format}% ({numTooleyVotes}) ")
print("---------------------------")
print(f"Winner: {maxvotes}")
print("---------------------------")
