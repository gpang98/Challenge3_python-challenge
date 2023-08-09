# Import os module to ease collaboration with others across operating systems
import os   

# import module for reading CSV files
import csv

#path does the smart way of going to the right directory
csvpath = os.path.join('Resources', 'budget_data.csv')   

# Initialize variables
total_change = 0      # set at 0
max_change = float()  # assigned as float number
min_change = float()  # assigned as float number
max_month = ""        # assigned as empty string
min_month = ""        # assigned as empty string

# Reading using CSV module
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader, None)

    # Read the first row to initialize previous_month_profit, Total_profit and num_months
    prev_month_profit = int(next(csvreader)[1])  # read index 1 and make it as integer
    Total_profit = prev_month_profit
    num_months = 1

    # Read each row of data after the header
    for row in csvreader:
        month, profit = row[0], int(row[1])  #assign row[0] as month & int(row[1]) as profit
        
        #compute change, total_change and Total_profit
        change = profit - prev_month_profit
        total_change += change
        Total_profit = Total_profit + profit
   
        #increment for the next month (row)
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

    #Output result into a folder and assigned txt file
    output_folder = "Analysis"
    output_file = os.path.join(output_folder, "result.txt")

    # create the output folder if does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # write the required text to the txt file
    with open(output_file, "w") as outfile:
        outfile.write(f"Financial Analysis\n")
        outfile.write(f"--------------------------------\n")
        outfile.write(f"Total Months: {num_months}\n")
        outfile.write(f"Total: ${Total_profit}\n")
        outfile.write(f"Average Change: $ {round(average_change,2)}\n")
        outfile.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
        outfile.write(f"Greatest Decrease in Profits: {min_month} (${min_change})")