# Andrew McCloud
# 09-12-2022
# Module 8 Assignment

# This assignment is to show how Try/Except blocks work and
# make a function that converts miles to Kilometers

# Make a constant for the conversion
MILES_TO_KILO = 1.609

# Create a function to get user input for miles
def MILES_OR_KILOMETERS():
    
    # Use Try/Except block to check the user input for a number
    try:

        # Ask the user if they want to convert from miles to kilometers 
        # or kilometers to miles
        userAnswer = int(input("Do you want to convert miles to kilometers (1) or kilometers to miles (2)? Please give us a 1 or a 2:"))

        
        # If the user inputs a 1, run this
        if userAnswer == 1:

            # Use a Try/Except block to check the user input for a number
            try:
                # Get user input for the amount of miles they want to convert
                miles = int(input("Please enter the number of miles you would like to convert to kilometers: "))

                # Call the mile to kilometers function with the amount of miles as the parameter
                miles_to_kilometers(miles)
            # If the user does not enter a number, shut down the application
            except:

                # Print the error message
                print("Error: User did not enter a number. Shutting down.")

        # Else, if the user inputs a 2, run this
        elif userAnswer == 2:

            # Use a Try/Except block to check the user input for a number
            try:
                # Get the user input for the amount of kilometers they want to convert to miles
                kilometers = float(input("Please enter the number of kilometers you would like to conver to miles: "))

                # Call the kilometers to miles function with the kilometers as the parameter
                kilometers_to_miles(kilometers)    

            # If the user does not enter a number, shut down the application    
            except:
                
                # Print the error message
                print("Error: User did not enter a number. Shutting Down")

        # Else, if the user does not input a 1 or a 2, tell them
        # and run the function again
        else:
            print("Please choose a 1 or a 2 ONLY")
            MILES_OR_KILOMETERS()

    # If the user does not enter a number for the miles to kilometers
    # or kilometers to miles, tell them what went wrong
    # and run the function again
    except:

        # Inform them what they did wrong
        print("Please only input a 1 or a 2!")

        # Run the function again
        MILES_OR_KILOMETERS()

    
# Create a function to convert miles to kilometers
# and display the results
def miles_to_kilometers(miles):

    # Convert the miles to kilometers
    kilometers = miles * MILES_TO_KILO

    # Display the results, only showing 3 decimal places
    print(miles, "mile(s) is", '{:,.3f}'.format(kilometers), "kilometers")

# Create a function to convert kilometers to miles
# and display the results
def kilometers_to_miles(kilometers):

    # Convert the kilometers to miles
    miles = kilometers / MILES_TO_KILO

    # Display the results, only showing 3 decimal places
    print(kilometers, "kilometers is", '{:,.3f}'.format(miles), "mile(s)")

# Call the MILES_OR_KILOMETERS function to start the application
MILES_OR_KILOMETERS()
