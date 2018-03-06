# Import dependencies
import os
import csv
from datetime import datetime

# Create new csv file to hold results
output_path = os.path.join('output', 'converted_employee_data.csv')

# Store file paths across operating systems
employee_csv_1 = os.path.join("raw_data", "employee_data1.csv")
employee_csv_2 = os.path.join("raw_data", "employee_data2.csv")

# Lists to store data
employee_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

# Set up dictionary for state abbreviations.
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

# Read through first csv
with open(employee_csv_1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row of the csv
    next(csvreader, None)
    
    for row in csvreader:
        
        # If there is already a row for this employee, skip it. Otherwise, add their info to each of the lists.
        new_id = int(row[0])
        if new_id not in employee_id:
            
            # Add their employee ID.
            employee_id.append(new_id)
            
            # Split the full name into first and last.
            name_string = row[1]
            full_name = name_string.split(" ")
            first_name.append(full_name[0])
            last_name.append(full_name[-1])
            
            # Read in date as datetime object, then save as string with different datetime format and add to list.
            birthday = datetime.strptime(row[2] , '%Y-%m-%d').strftime('%d/%m/%Y')
            dob.append(birthday)
            
            # Read in SSN as string, split using "-" as a delimeter, then save new SSN string hiding first 5 digits.
            # Add new SSN string to list.
            ssn_string = row[3]
            ssn_full = ssn_string.split("-")
            ssn_hidden = "***-**-" + ssn_full[-1]
            ssn.append(ssn_hidden)
            
            # Convert state from full name to abbreviation
            state.append(us_state_abbrev[row[4]])

# Read through second csv
with open(employee_csv_2, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row of the csv
    next(csvreader, None)
    
    for row in csvreader:
        
        # If there is already a row for this employee, skip it. Otherwise, add their info to each of the lists.
        new_id = int(row[0])
        if new_id not in employee_id:
            
            # Add their employee ID.
            employee_id.append(new_id)
            
            # Split the full name into first and last.
            name_string = row[1]
            full_name = name_string.split(" ")
            first_name.append(full_name[0])
            last_name.append(full_name[1:])
            
            # Read in date as datetime object, then save as string with different datetime format and add to list.
            birthday = datetime.strptime(row[2] , '%Y-%m-%d').strftime('%d/%m/%Y')
            dob.append(birthday)
            
            # Read in SSN as string, split using "-" as a delimeter, then save new SSN string hiding first 5 digits.
            # Add new SSN string to list.
            ssn_string = row[3]
            ssn_full = ssn_string.split("-")
            ssn_hidden = "***-**-" + ssn_full[-1]
            ssn.append(ssn_hidden)
            
            # Convert state from full name to abbreviation
            state.append(us_state_abbrev[row[4]])

# Zip lists together
clean_employee_data = zip(employee_id, first_name, last_name, dob, ssn, state)

# Write results to new csv file.
with open(output_path, 'w', newline="") as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvWriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

        # Write the zipped lists to a csv
        csvWriter.writerows(clean_employee_data)

