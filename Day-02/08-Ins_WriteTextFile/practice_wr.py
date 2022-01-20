#create filename variable 
outfile = open("file.txt", "w")

#Method 1 - Write to file and close it after
outfile.write("whats happening?")
outfile.close()

#method 2 - no need to add closing statement
#can add comma separators or \n for new line
with open("file.txt", "w")  as outfile:
    outfile.write("Yeah!") 
    outfile.write("Naaah")
    outfile.write("Ho\nHo\nHo")
