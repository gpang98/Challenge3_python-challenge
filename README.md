# Challenge3_python-challenge

##PyBank Code Explanation:
Input data is a csv file of two 'columns' of Date and Profit/Losses.  Total of 87 rows including the header.  
The following codes are constructed to do the following.

First few lines are to make sure necessary modules are imported to be able to read csv file in the assigned folder path independant of operating system.
1. Assigned some variables to store the data.
2. Read the csv file as an object.
3. Open the object file and do the following computation:
	- change, total_change and Total_profit
	- add month counter
	- Then loop thru the change value and assigned it as max_change or min_change to find the largest and smallest change
	- Compute average_change
4.  Assigned the output result in a folder as txt file.  Create the folder if it does not exist.
5.  Open the txt file and Write the required text as required.




##PyRoll Code Explanation:
Input data is a csv file of three 'columns' of Ballot ID, County and Candidate.  Total of 369,713 row including header and one empty line at the end.
The following codes are constructed to do the following.

First few lines to make sure necessary modules are imported to be able to read csv file in the assigned folder path independant of operating system.
1. Read the provided csv file into an object.
2. Four functions are created to read the object file to do the following:
	1. calculate_votes - to loop thru the data row by row and output total votes and candidate votes.
	2. calculate_percentage - use the result from step 2.1 to calculate the percentage for each candidate.
	3. find_winner - find the candidate with the most votes and return as winner
	4. write_results_to_file  - output all the required text as a txt file.

Run all the codes as main program and not as imported module.