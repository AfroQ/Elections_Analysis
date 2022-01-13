# @TODO: Your code here
# Create a dictionary to store the following:
# Your name
# Your age
# A list of a few of your hobbies
# A dictionary of a few times you wake up during the week
# Print out your name, how many hobbies you have 
# and a time you get up during the week.

my_info = {
    "name": "Meoskers",
    "Age": 105,
    "Hobbies": ["climbing", "licking", "scratching"],
    "Wakeup":{"Mon": 12, "Friday": 1, "Sat": 4}
}

print(f"My name is {my_info['name']}. I have {len(my_info['Hobbies'])} hobbies")
print(f"On the weekend, I wake up at {my_info['Wakeup']['Sat']}")