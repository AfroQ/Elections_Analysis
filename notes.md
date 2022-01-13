# **Common terminal commands** 

```python
`pwd` will shows the current directory

`cd Desktop` will change to the desktop directory

`mkdir <folder_name>` will make a new directory/folder on the desktop.

`cd <folder_name>` will move to the newly created folder

`open .` on a Mac will open the current folder

`explorer .` on a Windows will open the current folder

`code .` will opens the current directory in VS Code

`touch <file_name.py>` will create a Python file

`ls` will show what is in the current directory

`cd ..` will move us up a directory back to Desktop

```

# Variables

```python
# Creates a variable with a string "Frankfurter"
title = "Frankfurter"

# Creates a variable with an integer 80
years = 80

# Creates a variable with the boolean value of True
expert_status = True

# Prints a statement adding the variable
print("Nick is a professional " + title)

# Convert the integer years into a string and prints
print("He has been coding for " + str(years) + " years")

# Converts a boolean into a string and prints
print("Expert status: " + str(expert_status))

# An f-string accepts all data types without conversion
print(f"Expert status: {expert_status}")
```

# Lists

- Lists are very flexible, you can store so many different data types in them. 
- You extract the data by number (index) eg. grocery_list[3]

```
# Create a Python list to store your grocery list
grocery_list = ["milk", "Bread", "Eggs", "Peanut Butter", "Jelly"]

# Print the grocery list
print(grocery_list)

# Change "Peanut Butter" to "Almond Butter" and print out the updated list
grocery_list[3]= "Almond Butter"

# Remove "Jelly" from grocery list and print out the updated list
grocery_list.remove("Jelly")

# Add "Coffee" to grocery list and print the updated list
grocery_list.append("Coffee")
print(grocery_list)
```

# Dictionaries

Create a list of key value pairs

```python
# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------

# A list of actors
actors = ["Tom Cruise",
          "Angelina Jolie",
          "Kristen Stewart",
          "Denzel Washington"]

# A dictionary of an actor
actor = {"name": "Tom Cruise"}
print(f'{actor["name"]}')

# ---------------------------------------------------------------

# A dictionary can contain multiple pairs of information
actor_info = {
    "name": "Angelina Jolie",
    "genre": "Action",
    "nationality": "United States"
}

# ---------------------------------------------------------------

# A dictionary can contain multiple types of information
another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best movies": [
        "Rocky",
        "Rocky 2",
        "Rocky 3"]}
print(f'{another_actor["name"]} was in {another_actor["best movies"][0]}')
# ---------------------------------------------------------------

# A dictionary can even contain another dictionary
film = {
    "title": "Interstellar",
    "revenues": {
        "United States": 360,
        "China": 250,
        "United Kingdom": 73
    }
}
print(f'{film["title"]} made {film["revenues"]["United States"]}'" in the US.")
# ---------------------------------------------------------------

```

# Reading CSV

```python
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'accounting.csv')

# # Method 1: Plain Reading of CSV files
with open(csvpath, 'r') as file_handler:
     lines = file_handler.read()
     print(lines)
     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

```

