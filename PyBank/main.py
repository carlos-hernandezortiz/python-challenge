#Libraries importing
import os
import csv
#File's Path
csvpath = os.path.join('C:/Users/empha/Desktop/Data_Analytics/Semana_4/python-challenge/PyBank/','Resources', 'Lessons_03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
output_path =  os.path.join('C:/Users/empha/Desktop/Data_Analytics/Semana_4/python-challenge/PyBank/','analysis','analysis.txt')
#opening our file to read
with open(csvpath,'r',newline='', encoding='utf-8') as csvfile:
    #csvfunction to read for each coma
    csvreader = csv.reader(csvfile,delimiter=',')
    #removing the header
    csvheader = next(csvreader)
    #defining the variables needed for the program (also lists, which will store the months an profits extracted from csv file)
    months_counter = 0
    net_total = 0
    profits_list = []
    months_list = []
    months_change_recorder = []
    changes_list = []
    #reading each row from csv file
    for rows in csvreader:
        #getting the length of the csv file
        months_counter +=1
        #calculating the total of the profits/losses column
        net_total += int(rows[1])
        #extracting the profit/loss and storing it on a list.
        profits_list.append(int(rows[1]))
         #extracting the period and storing it on a list.
        months_list.append(rows[0])
    
    #looping to get the difference from the next period to the actual period and storing this value and the corresponding month on a list
    for i in range(len(profits_list)):
        if  i < (months_counter-1):
            change_recorder = profits_list[i+1] - profits_list[i]
            changes_list.append(change_recorder)
            months_change_recorder.append(months_list[i+1])
            
    #calculating the data required using basic operations 
    average_change = round(sum(changes_list)/len(changes_list),2)
    greatest_change = max(changes_list)
    index_increase = changes_list.index(greatest_change)
    greatest_decrease = min(changes_list)
    index_decrease = changes_list.index(greatest_decrease)
    month_increase = months_change_recorder[index_increase]
    month_decrease = months_change_recorder[index_decrease]
#printing on console
print("Financial Analysis")
print("-------------------------------")   
print(f'Total Months: {months_counter}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {month_increase} (${greatest_change})')
print(f'Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})') 

#writing on text files
with open(output_path, "w", newline='',encoding='utf-8\n') as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("-------------------------------\n")
    datafile.write(f'Total Months: {months_counter}\n')
    datafile.write(f'Total: ${net_total}\n')
    datafile.write(f'Average Change: ${average_change}\n')
    datafile.write(f'Greatest Increase in Profits: {month_increase} (${greatest_change})\n')
    datafile.write(f'Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})\n')
