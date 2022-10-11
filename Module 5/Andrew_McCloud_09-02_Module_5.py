# With this code, we are taking user input
# and finding prices for customers

# Andrew McCloud
# 09-02-2022
# Module 5 Assignment

# Create a constant for our conversion 
COST_PER_FOOT = 0.87
# Constant for the discounted price for over 100 feet
PRICE_PER_FOOT_OVER_100 = 0.80
# Constant for the discounted price for over 250 feet
PRICE_PER_FOOT_OVER_250 = 0.70
# Constant for the discounted price for over 500 feet
PRICE_PER_FOOT_OVER_500 = 0.50

# Give a welcome message
print("Welcome to the Company Calculator!")

# Get the user input
companyName = input("\nWhat is the name of your company? ")

# Print a welcome to the user from the company name
print("\nThank you for joing us from ", companyName,"\n")

# Print the price menu for the user
print("""XXXXXXXXXXXXXX-Cost Menu-XXXXXXXXXXXXXX
|  Length                Cost per Foot|
|length < 100 FT ----------- $0.87    |
|100ft < length < 250ft ---- $0.80    |
|250ft < length < 500ft ---- $0.70    |
|length > 500ft ------------ $0.50    |
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n""")

# Get the number of feet for optic to be installed
fiberLength = float(input("Please give us the length of fiber needed to be installed: "))

# If the fiber length is greater than 100 feet and less than 250 feet,
# give the minimum discount
if fiberLength > 100 and fiberLength < 250:

    # Inform the user how much it costs with the discount
    print("\nSince your length is greater than 100 feet, the discounted price is $0.80 per foot.")

    # Calculate the total cost of the price
    convertedPrice = fiberLength * PRICE_PER_FOOT_OVER_100

# Else is, thefiber length is greater than 250 feet and less than 500 feet
# discount the price to $0.70 per foot
elif fiberLength > 250 and fiberLength < 500:

     # Inform the user how much it costs with the medium discount
    print("\nSince your length is greater than 250 feet, the discounted price is $0.70 per foot.")

    # Calculate the total cost of the price
    convertedPrice = fiberLength * PRICE_PER_FOOT_OVER_250

# Else if, the fiber length is greater than 500 feet,
# discount the price to $0.50 per foot
elif fiberLength > 500:

    # Inform the user how much it costs with the biggest discount
    print("\nSince your length is greater than 500 feet, the discounted price is $0.50 per foot.")

    # Calculate the total cost of the price
    convertedPrice = fiberLength * PRICE_PER_FOOT_OVER_500

# Else statement is used for if the fiber length is less than 100 feet
# so that the discount is not given
else:

    # Inform the user how much we charge per foot without discount
    print("\nWe charge $0.87 per foot since your length is less than 100 feet.")

    # Convert the total cost
    convertedPrice = fiberLength * COST_PER_FOOT


#Display how much it will cost the customer
# The ${:,.2f} allows us to format the number into a dollar amount to the nearest 2 decimals
print("\nIt will cost you ", '${:,.2f}'.format(convertedPrice), " for ", companyName, " to have ", fiberLength , " feet installed.\n")
