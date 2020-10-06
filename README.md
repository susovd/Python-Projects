<!---Project Logo -->
<br />
<p align="center">
  <h3 align="center">Python projects to analyze bank performance and poll counts.</h3>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Results](#results)


<!-- ABOUT THE PROJECT -->
## About The Project

## Background


In this project, I have completed the **two** Python Challenges, PyBank and PyPoll. There are two folders, Pybank and Pypoll, each folder corresponding to each project. 

* Inside of each folder contains:

  * A file called `main.py`. It contains the main script to run for each analysis.
  * A "Resources" folder that contains the CSV files I used. 
  * An "analysis" folder that contains text file that has the results from my analysis.

## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this project, I created a Python script for analyzing the financial records of a company. It will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

* My python script analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* In addition, my final script prints the analysis to the terminal and exports a text file with the results.

## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this project, I am helping a small, rural town modernize its vote counting process.

* I have a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. I created a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* In addition, my final script prints the analysis to the terminal and exports a text file with the results.

### Built With
* [Python](https://www.python.org/about/)


## Results
My analysis of the banks gave me the following output.

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```
 

My analysis of the polls gave me the following output.

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

**Additional reference materials:**

_Best-README-Template_ Retrieved from: [https://github.com/othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template)
