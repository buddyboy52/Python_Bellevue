# Andrew McCloud
# 09-03-2022
# Module 6: Dictionaries

# The purpose of this assignment is to learn how dictionaries work in Python

class dictionaries:

    # Create a dictionary for car makes
    car_models = {1: 'Chevrolet', 2: 'Ford', 3: 'Pontiac', 4: 'Audi',
                  5: 'Dodge', 6: 'Cadillac', 7: 'Buick', 8: 'Jeep', 9: 'Bugatti', 10: 'BMW'}

    # Display the car model dictionary
    print(car_models)

    # Ask the user to select a choice from the dictionary
    userChoice = int(input("Please pick a car make from the above options: "))

    # Print what the user chose from the dictionary
    print("Since you chose ", userChoice,
          ", your car make is ", car_models[userChoice])
