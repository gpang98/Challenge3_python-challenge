# Import os module to ease collaboration with others across operating systems
import os   

# import module for reading CSV files
import csv

#path does the smart way of going to the right directory
csvpath = os.path.join('Resources', 'election_data.csv')   

# define a function to total up votes per candidate and grand total
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
            # count the votes for each candidate in a dictionary
            # candiate is the name of the candidate
            # if candidate does not exist as a key in the dictrinary then it will return 0 
            # else +1 if the candidate received another vote
            candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1    
    # return the total votes and dictionary candidate_votes that hold the vote counts per candidate
    return total_votes, candidate_votes

# define function to calculate percentage of votes 
def calculate_percentage(votes, total):
    return (votes / total) * 100

# define function to find winner with maximum votes from candidate_votes dictionary
def find_winner(candidate_votes):
    # Find the candidate with the highest votes
    winner = max(candidate_votes, key=candidate_votes.get)
    return winner

# define output file with folder and print out the required tabulation.
def write_results_to_file(total_votes, candidate_votes):
    output_folder = "Analysis"
    output_file = os.path.join(output_folder, "result.txt")

    # create new folder if does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # open output text file to output result
    with open(output_file, "w") as outfile:
        outfile.write(f"Election Results\n")
        outfile.write(f"-------------------------\n")
        outfile.write(f"Total Votes: {total_votes}\n")
        outfile.write(f"-------------------------\n")

        # loop through the result per candidate in the dictionary to calculate percentage
        for candidate, votes in candidate_votes.items():
            percentage = calculate_percentage(votes, total_votes)
            outfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        outfile.write(f"-------------------------\n")

        # print out the winner
        outfile.write(f"Winner: {winner}\n")
    
        outfile.write(f"-------------------------\n")

# making sure that the code is being run as the main program and not imported as module
if __name__ == "__main__":
    total_votes, candidate_votes = calculate_votes(csvpath) # run calculate_votes function and output total votes and candidate votes
    winner = find_winner(candidate_votes)                   # run find_winner function and output winner
    write_results_to_file(total_votes, candidate_votes)     # run write_to_results_to_file function