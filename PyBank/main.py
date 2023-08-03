# First we'll import the os module
# This will allow us to create file paths across operating systems
import os   # help in collaboration with others

# Module for reading CSV files
import csv

#path does the smart way of going to the right directory
csvpath = os.path.join('Resources', 'budget_data.csv')   

# Initialize variables
total_change = 0
max_change = float('-inf')
min_change = float('inf')
max_month = ""
min_month = ""

# Method 2: Improved Reading using CSV module

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader, None)

    # Read the first row to initialize previous_month_profit, Total_profit and num_months
    prev_month_profit = int(next(csvreader)[1])
    Total_profit = prev_month_profit
    num_months = 1

    # Read each row of data after the header
    for row in csvreader:
        month, profit = row[0], int(row[1])
        
        #print(f"{month}  + {profit}")
        change = profit - prev_month_profit
        #print(f"{profit}  + {prev_month_profit}")
        total_change += change
        Total_profit = Total_profit + profit #int(row[1])
   
        num_months = num_months + 1

        # Check if the change is the new max or min
        if change > max_change:
            max_change = change
            max_month = month
        if change < min_change:
            min_change = change
            min_month = month

        # Update previous_month_profit for the next iteration
        prev_month_profit = profit
    # number of months need to minus 1 because no of changes is one less than total no of months
    average_change = total_change / (num_months - 1)

# print the result
print()

print(f"Financial Analysis\n")
print("--------------------------------\n")

print(f"Total Months: {num_months}\n")

print(f"Total: ${Total_profit}\n")

print(f"Average Change: $ {round(average_change,2)}\n")

print(f"Greatest Increase in Profits: {max_month} $ {max_change}\n")

print(f"Greatest Decrease in Profits: {min_month} $ {min_change}")