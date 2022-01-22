import os
import csv

# Assign a variable for the file to load and the path.
election_file = os.path.join('Resources', 'election_results.csv')

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize variable to contain total votes
total_votes = 0

# Declare a new list to hold candidate names
candidate_options = []

# Initialize dict to hold total votes per candidate
candidate_votes = {}

county_options = []

votes_per_county = {}

# Open the election results and read the file.
with open(election_file) as election_data:
    file_reader = csv.reader(election_data)
        # Print the header row.
    headers = next(file_reader)
    #print(headers)
#    for row in file_reader:
#        print(row)

    #Total number of votes cast
    #Loop through all rows, adding to total for very row
    for row in file_reader:
        #Add to vote count
        total_votes += 1
    
        #A complete list of candidates who received votes  
        #print candidate name for each row
        candidate_name = row[2]
        county_name = row[1]

        #get each unique candidate name 
        if candidate_name not in candidate_options:
            #add candidate name to the candidate list 
            candidate_options.append(candidate_name)
            
            #initialize tracker for votes per candidate
            candidate_votes[candidate_name] = 0
    
        #For each unique candidate name, sum up every time they appear
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        if county_name not in county_options:
            county_options.append(county_name)
            votes_per_county[county_name] = {}
        if candidate_name not in votes_per_county[county_name]:
            votes_per_county[county_name][candidate_name] = 0
        votes_per_county[county_name][candidate_name] += 1

print(total_votes)
print(candidate_options)
print(candidate_votes)
print(county_options)
print(votes_per_county)

# Percentage of votes each candidate won
# 4. Each candidate total divide by total votes
# 5. format as percentage

# The winner of the election based on popular vote
# 5. Compare all candidate totals
# 6. Get max count name -->