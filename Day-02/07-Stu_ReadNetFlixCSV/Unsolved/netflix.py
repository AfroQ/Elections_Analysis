# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")
print(csvpath)

# Open the CSV
with open(csvpath) as file_reader:
    # Loop through looking for the video
    csvreader = csv.reader(file_reader, delimiter = ',')
    for row in csvreader:
        if row[0] == video:
            print(f"{row[0]} came out in {row[4]} and is rated {row[1]}")
    else:
        print("We couldn't find the video, try another title!")

