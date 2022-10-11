# Andrew McCloud
# 09-29-2022
#
# Module 11 Buggy Assignment

# This program has a bug in it and users need to fix it

# Declare a constant for how many seconds in a minute
SECONDS_IN_A_MINUTE = 60


# Create a function to convert minutes to hours
def conversion():

    minutes = float(input("Please input a number of minutes: "))

    # Convert the minutes into seconds
    seconds = minutes * SECONDS_IN_A_MINUTE

    # Call the printSeconds function
    printSeconds()

# Create a printSeconds function to display the seconds


def printSeconds(seconds):

    print(seconds)


# Start the program by running the conversion function
conversion()
