#Libraries importing
import os
import csv
#File's Path
csvpath = os.path.join('C:/Users/empha/Desktop/Data_Analytics/Semana_4/python-challenge/PyPoll/','Resources', 'Lessons_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
output_path =  os.path.join('C:/Users/empha/Desktop/Data_Analytics/Semana_4/python-challenge/PyPoll/','analysis','analysis.txt')
#opening our file to read
with open(csvpath,'r',newline='', encoding='utf-8') as csvfile:
    #csvfunction to read for each coma
    csvreader = csv.reader(csvfile,delimiter=',')
    #removing the header
    csvheader = next(csvreader)
    #defining variables that will help us in the loop
    total_rows = 0
    #looping through all the records and counting them. Finding unique candidates and creating a dictionary for them and adding values.
    unique_candidates = {}
    for row in csvreader:
        total_rows+=1
        if row[2] not in unique_candidates:
            unique_candidates[row[2]] = 0
        unique_candidates[row[2]] +=1
#priting on console and writing on csv file
with open(output_path, "w", newline='',encoding='utf-8\n') as datafile:
    #prints
    print("Election Results")
    print("-------------------------------") 
    print(f'Total Rows: {total_rows}')
    print("-------------------------------")
    #writes
    datafile.write("Election Results\n")
    datafile.write("-------------------------------\n")
    datafile.write(f'Total Rows: {total_rows}\n')
    datafile.write(f'-------------------------------\n')
    max_votes = 0
    #getting winner and printing in console each candidate and their votes.
    for candidate in unique_candidates:
        if unique_candidates[candidate]> max_votes:
            max_votes = unique_candidates[candidate]
            person = candidate
        percentage_voting = round(float(unique_candidates[candidate]/total_rows)*100,3)
        print(f'{candidate}: {percentage_voting}%   ({unique_candidates[candidate]})')
        datafile.write(f'{candidate}: {percentage_voting}%   ({unique_candidates[candidate]})\n')
    #prints
    print("-------------------------------")
    print(f'Winner: {person}')
    #writes
    datafile.write("-------------------------------\n")
    datafile.write(f'Winner: {person}\n')




