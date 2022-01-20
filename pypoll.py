import os
import csv

# Assign a variable for the file to load and the path.
election_file = os.path.join('Resources', 'election_results.csv')

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(election_file) as election_data:
    file_reader = csv.reader(election_data)
        # Print the header row.
    headers = next(file_reader)
    print(headers)
#    for row in file_reader:
#        print(row)
# Total number of votes cast
# 1. initialize variable to contain total votes
# 2. Loop through all rows, adding to total for very row

# A complete list of candidates who received votes
# 1. count each unique candidate name

# Total number of votes each candidate received
# 2. Initialize variable to hold total per candidate
# 3. For each unique candidate name, sum up every time they appear

# Percentage of votes each candidate won
# 4. Each candidate total divide by total votes
# 5. format as percentage

# The winner of the election based on popular vote
# 5. Compare all candidate totals
# 6. Get max count name -->