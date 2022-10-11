# Import the OS Library so we can read and write to files
import os

# Get the speciifed file path from the user
filePath = input("Where is the location that you would like to save your file? ")

# Inform the user of the file path they have typed in
print("The directory you have chosen is: ", filePath)

# Get a file name for the new file
fileName = input("What would you like to name this file? ")

# Add .txt to the end of the file so it creates a text file
completeName = fileName + ".txt"

# Get the name of the user to write to the file
name = input("What is your first name? ")

# Get the address of the user to write to the file
address = input("What is your address? ")

# Get the phonenumber of the user to write to the file
phoneNumber = input("What is your phone number? (Without dashes) ")

information = ("Name: "+ name + " Address: " + address + " Phone Number: "+ phoneNumber)

# Save the file with the new file name in the specified directory
file = os.path.join(filePath, completeName)

# Open the file so we can write to it
writeFile = open(file, "w")

# Write the name to the file
writeFile.write(information)

# Close the file because it could only be written to
writeFile.close()

# Open the file in read only format
writeFile = open(file, "r")

# Read the file
print(writeFile.read())
