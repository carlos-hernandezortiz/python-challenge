#Importing libraries
import os
import csv
#States Dictionary: obtained from-https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
#File's Path
csvpath = os.path.join('C:/Users/empha/Desktop/Data_Analytics/Semana_4/python-challenge/PyBoss/','Resources', 'Lessons_03-Python_Homework_ExtraContent_Instructions_PyBoss_employee_data.csv')
output_path =  os.path.join('C:/Users/empha/Desktop/Data_Analytics/Semana_4/python-challenge/PyBoss/','Output','Output.csv')
emp_id_list = []
first_name_list = []
last_name_list = []
dob_list = []
ssn_list = []
state_list = []

#opening our file to read
with open(csvpath,'r',newline='', encoding='utf-8') as csvfile:
    #csvfunction to read for each coma
    csvreader = csv.reader(csvfile,delimiter=',')
    #removing the header
    csvheader = next(csvreader)
    #
    for row in csvreader:
        emp_id_list.append(row[0])
        first_name_list.append(row[1].split(" ")[0])
        last_name_list.append(row[1].split(" ")[1])
        dob_original = row[2].split("-")
        dob_modified = str(dob_original[1]+"/"+dob_original[2]+"/"+dob_original[0])
        dob_list.append(dob_modified)
        ssn_original = row[3].split("-")
        ssn_modified = "***"+"-"+"**"+"-"+ssn_original[2]
        ssn_list.append(ssn_modified)
        state_list.append(us_state_abbrev[row[4]])
    output = zip(emp_id_list,first_name_list,last_name_list,dob_list,ssn_list,state_list)
#writing on text files
with open(output_path, "w", newline='',encoding='utf-8\n') as datafile:
    writer =csv.writer(datafile)
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    writer.writerows(output)

        





    

