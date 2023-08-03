# First we'll import the os module
# This will allow us to create file paths across operating systems
import os   # help in collaboration with others

# Module for reading CSV files
import csv

#path does the smart way of going to the right directory
csvpath = os.path.join('Resources', 'election_data.csv')   


def calculate_votes(csvpath):
    # Initialize variables
    total_votes = 0
    candidate_votes = {}

    # Open the CSV file
    with open(csvpath, newline='') as csvfile:
        # Create a CSV reader
        reader = csv.reader(csvfile)

        # Skip the header row
        next(reader, None)

        # Loop through the rows
        for row in reader:
            candidate = row[2]
            total_votes += 1
            candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

    return total_votes, candidate_votes

def calculate_percentage(votes, total):
    return (votes / total) * 100

if __name__ == "__main__":
    #filename = "data.csv"
    total_votes, candidate_votes = calculate_votes(csvpath)

    print("Total votes:", total_votes)
    print("Votes for each candidate with their percentages:")

    for candidate, votes in candidate_votes.items():
        percentage = calculate_percentage(votes, total_votes)
        print(f"{candidate}: {votes} votes, {percentage:.2f}%")
