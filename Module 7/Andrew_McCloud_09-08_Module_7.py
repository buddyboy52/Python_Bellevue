# Andrew McCloud
# 09-08-2022
# Module 7 Assignment

# The purpose of this code is to demonstrate how while loops work

# Create a constant for the investment with a 7% interest rate added on
from operator import inv

# Get the user input for the initial investment
investment = float(input("What was your initial investment: "))

# Get the interest rate from the user
interestRate = float(input(
    "Please tell us the interest rate of the investment (with whole numbers):"))

# Convert the interest rate into a decimal
interestRate = interestRate / 100

# Create a varible for the double investment
# Do not set it to a hard value, if we change the investment var,
# it will change this value
doubledInvestment = investment * 2

# Create a variable to track the number of years
yearCount = 0

# Create our while loop to loop through years and
# adding interest to the investment
while investment <= doubledInvestment:

    # Add one to the year count
    yearCount = yearCount + 1

    # Add the 7% interest to the investment
    investment = (investment * interestRate) + investment

    print(investment, " after year", yearCount)

print("\nYour investment has doubled in", yearCount, "years at",
      (interestRate * 100), "percent interest rate.")
