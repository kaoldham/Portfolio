# Import dependencies
import os
import csv
from datetime import datetime

# Create new text file to hold results
output_path = os.path.join('output', 'financial_analysis.txt')

# Store file paths across operating systems
revenue_csv_1 = os.path.join("raw_data", "budget_data_1.csv")
revenue_csv_2 = os.path.join("raw_data", "budget_data_2.csv")

# Lists to store data
date = []
revenue = []
rev_changes = []

# Read through first csv
with open(revenue_csv_1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row of the csv
    next(csvreader, None)
    
    for row in csvreader:
        
        # If there is already data for this month, add revenue to that date's total revenue.
        new_date = datetime.strptime(row[0], '%b-%y')
        if new_date in date:
            revenue[date.index(new_date)] = revenue[date.index(new_date)] + int(row[1])
            
         # Otherwise, add date/revenue. Convert date to datetime object without time.
        else:
            date.append(datetime.strptime(row[0] , '%b-%y'))
        
            # And add revenue as integer
            revenue.append(int(row[1]))

# Read through second csv
with open(revenue_csv_2, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row of the csv
    next(csvreader, None)
    
    for row in csvreader:
        
        # If there is already data for this month, add revenue to that date's total revenue.
        new_date = datetime.strptime(row[0], '%b-%Y')
        if new_date in date:
            revenue[date.index(new_date)] = revenue[date.index(new_date)] + int(row[1])
        
        # Otherwise, add date/revenue. Convert date to datetime object without time.
        else:
            date.append(datetime.strptime(row[0], '%b-%Y'))
            
            # And add revenue as integer
            revenue.append(int(row[1]))

# Count number of months for which we have revenue data.
num_months = len(date)

# Calculate total revenue
total_rev = sum(revenue)

# Before calculating monthly changes in revenue, we need to sort by date.

# First, zip my date/revenue info together into tuples
rev_data = zip(date, revenue)

# Then sort by date
rev_data_sorted = sorted(rev_data, key=lambda date: date[0])

# Now cycle through calculating each change in revenue
# Also keep tabs on max/min change and their dates
for idx, val in enumerate(rev_data_sorted):
    
    # Make sure you haven't reached the last item in the list
    # (Can't calculate change if we don't know the next month's data)
    if val != rev_data_sorted[-1]:
        
        # if this is the first iteration, set max and min change = this month's change to start.
        if len(rev_changes) == 0:
            max_change = rev_data_sorted[idx+1][1]-rev_data_sorted[idx][1]
            max_date = rev_data_sorted[idx+1][0].strftime('%b-%y')
            min_change = rev_data_sorted[idx+1][1]-rev_data_sorted[idx][1]
            min_date = rev_data_sorted[idx+1][0].strftime('%b-%y')
        
        # After first iteration, check whether this is a new max change
        if len(rev_changes)>0 and max(rev_changes) < rev_data_sorted[idx+1][1]-rev_data_sorted[idx][1]:
            max_change = rev_data_sorted[idx+1][1]-rev_data_sorted[idx][1]
            max_date = rev_data_sorted[idx+1][0].strftime('%b-%y')
        
        # After first iteration, check whether this is a new min change
        if len(rev_changes)>0 and min(rev_changes) > rev_data_sorted[idx+1][1]-rev_data_sorted[idx][1] or len(rev_changes)==0:
            min_change = rev_data_sorted[idx+1][1]-rev_data_sorted[idx][1]
            min_date = rev_data_sorted[idx+1][0].strftime('%b-%y')
        
        # Now add the most recent monthly change to the list of monthly changes to prepare
        # for the next iteration and calculating the overall avg. monthly change.
        rev_changes.append(rev_data_sorted[idx+1][1]-rev_data_sorted[idx][1])
     
# Find avg. revenue change.
avg_change = sum(rev_changes)/len(rev_changes)

# Print results to console.
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(num_months))
print("Total Revenue: $" + str(total_rev))
print("Average Revenue Change: $" + str(round(avg_change)))
print("Greatest Increase in Revenue: " + max_date + " $" + str(max_change))
print("Greatest Decrease in Revenue: " + min_date + " $" + str(min_change))

# Print results to text file.

# Open output file for writing.
output = open(output_path, "w")

# Print results to file.
output.write("Financial Analysis\n")
output.write("----------------------------\n")
output.write("Total Months: " + str(num_months) + "\n")
output.write("Total Revenue: $" + str(total_rev) + "\n")
output.write("Average Revenue Change: $" + str(round(avg_change)) + "\n")
output.write("Greatest Increase in Revenue: " + max_date + " $" + str(max_change) + "\n")
output.write("Greatest Decrease in Revenue: " + min_date + " $" + str(min_change))

output.close()

