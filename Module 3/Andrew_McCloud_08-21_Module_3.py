# With this code, we are taking user input
# and finding prices for customers

# Create a constant for our conversion 
COST_PER_FOOT = 0.87

# Give a welcome message
print("Welcome to the Company Calculator!")

# Get the user input
companyName = input("\nWhat is the name of your company?")

# Print a welcome to the user from the company name
print("\nThank you for joing us from ", companyName)

# Get the number of feet for optic to be installed
fiberLength = float(input("Please give us the length of fiber needed to be installed: "))

# Inform the user how much we charge per foot
print("\nWe charge $0.87 per foot")

# Convert the total cost
convertedPrice = fiberLength * COST_PER_FOOT

#Display how much it will cost the customer
# The ${:,.2f} allows us to format the number into a dollar amount to the nearest 2 decimals
print("\nIt will cost you ", '${:,.2f}'.format(convertedPrice), " for ", companyName, " to have ", fiberLength , " feet installed.")
