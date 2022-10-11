# Andrew McCloud
# 08-27-22
# Module 4 Assignment

# The purpose of this code is demonstrate how tuples work

# Initialize my tuple
statesTuple = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
                'Colorado', 'Conneticut', 'Delaware', 'Florida', 'Georgia',
                'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
                'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massacusetts',
                'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
                'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexcio',
                'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
                'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
                'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
                'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')

# Print the header for the tuple display
print("\n----- The tuple display -----")

# Display the contents in a single statement
print(statesTuple)

# Assign a variable to length of the statesTuple
# This makes it so we can use that later if needed
numOfStates = len(statesTuple)

# Print the header to the for the states in their own sentences
print("\n----- The states in their own sentences -----")

# Use a for loop to print the states
for x in range(numOfStates):
   print(f"|| {statesTuple[x]} is in the {x + 1} position alphabetically.")

# Print a header for the states in reverse
print("\n----- The states in reverse -----")

# Use a for loop to reverse the states
# Using range, we set the starting point as 49,
# the ending point as -1 so we can display 0 without it stopping,
# and the third slot tells it to go down one each time
for x in range(49, -1, -1):
    print(f"|| In position {x + 1} is {statesTuple[x]}")

