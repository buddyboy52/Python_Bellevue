# Andrew McCloud
# 09-24-2022
# Module 9 Assignment

# The purpose of this code is to help us understand how classes work and
# use them for bank accounts

# Create our constants
MINIMUM_ALLOWED = 50
INTEREST_RATE = 0.02
FEE = 5
BIG_ACCOUNT_AMOUNT = 200
SMALL_ACCOUNT_AMOUNT = 25
BIG_ACCOUNT_NUMBER = 20202
SMALL_ACCOUNT_NUMBER = 10101

# Create a class for our bank account


class BankAccount:

    # Create our init function for self
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    # Create a function to withdraw money

    # Create a function for withdrawl so the user can withdrawl money
    def withdrawl(self):

        # Use try/except to make sure the user input is only numbers
        try:

            # Get user input for the amount of money to be withdrawn
            money_withdrew = float(
                input("How much would you like to withdraw? "))

        # Give an error if the user enters in something besides numbers
        except ValueError:
            print("Please only enter in numbers!")

            bank_account = BankAccount(self.accountNumber, self.balance)

            # Run the withdrawl again so that they can re-input numbers
            bank_account.withdrawl()

        # Calculate the new account balance
        new_balance = self.balance - money_withdrew

        # Make sure that they account does not go negative or under the limit
        # Use a while loop to make sure the user does not go below $0
        while new_balance < 0:

            # Inform the user that their account will be negative and
            # they cannot withdrawl that amount
            print("Your balance will be", '${:,.2f}'.format(
                new_balance), "and you cannot go below $0.")

            # Prompt the user for how much they would like to withdraw
            money_withdrew = float(
                input("\nHow much money would you like to withdraw?"))

            # Calculate the new balance (again)
            new_balance = self.balance - money_withdrew

        # Inform the user on how much they withdrew from their account
        print("Congrats on withdrawing", '${:,.2f}'.format(
            money_withdrew), "from your account. You now have", '${:,.2f}'.format(new_balance), "in your account!")

        # Create a checking account variable and set it to the CheckingAccount class
        userChecking = CheckingAccount(self.accountNumber, new_balance)

        # Call the checkMinimumBalance function
        userChecking.checkMinimumBalance()

        # Run the runAgain function
        runAgain()

    # Create a deposit function to allow the user to deposit money into the account
    def deposit(self):

        # Use try/except to make sure the user only enters numbers in for the deposit amount
        try:
            # Get the amount for how much the user wants to deposit
            depositAmount = float(
                input("How much money would you like to deposit? "))

        except:

            # If the user does not enter numbers, prompt an error
            print("Please only use numbers!")

            # Rerun the deposit function
            self.deposit()

        # Calculate the new account balance
        newBalance = self.balance + depositAmount

        # Inform the user what is happening to their account
        print("\nYou are depositing", '${:,.2f}'.format(
            depositAmount), "into account", self.accountNumber)

        print("\nThis will make your balance",
              '${:,.2f}'.format(newBalance))

        runAgain()

    def getBalance(self):

        print("The balance of your account is",
              '${:,.2f}'.format(self.balance))

        runAgain()


# Create our class for the bank account
class CheckingAccount(BankAccount):

    # Create our init function for self
    def __init__(self, accountNumber, balance):
        super(CheckingAccount, self).__init__(accountNumber, balance)
        self.fees = FEE
        self.minimum_balance = MINIMUM_ALLOWED

    # Create a deductFees method to deduct money for withdrawing
    def deductFees(self):

        # Prompt the user the fees it will cost to take money out of your account
        print("It will cost $5 to withdraw money from your checking account.")

    # Create a checkMinimumBalance function to check minimum balance
    def checkMinimumBalance(self):

        # If the balance is greater than the minimum allowed, do nothing
        if self.balance >= MINIMUM_ALLOWED:

            # Calculate how much more money they have than the minimum balance
            balanceDifference = self.balance - MINIMUM_ALLOWED

            print("\nYou have", balanceDifference,
                  "until you go under the minimum amount allowed in an account.")

        # Else, if the balance is lower than the minimum allowed, prompt the user
        else:
            print(
                "Your account is below the minimum balance allowed. Please fix immediatley.")


# Create our class for the savings account
class SavingsAccount(BankAccount):

    # Create our init function for self
    def __init__(self, accountNumber, balance):
        super(SavingsAccount, self).__init__(accountNumber, balance)
        self.interestRate = INTEREST_RATE

    # Create a function to add interest to the savings account
    def addInterest(self):

        # Calculate the interest
        interest = INTEREST_RATE * self.balance

        # Add the interest to the balance
        newBalance = self.balance + interest

        # Display the new balance
        print("Your savings account has a balance of", '${:,.2f}'.format(
            newBalance), "after", INTEREST_RATE, "% interest rate")

# Create a big account function to run for the big account with $200


def big_account(accountNumber):

    # Create a checking account variable and set it to the CheckingAccount class
    userChecking = CheckingAccount(accountNumber, BIG_ACCOUNT_AMOUNT)

    # Call the checkMinimumBalance function
    userChecking.checkMinimumBalance()

    # Get user input for the user choice to ask them if they would like to
    # Withdrawl, deposit,, or check balance
    userChoice = input(
        "Welcome to your account. Would you like to Withdrawl (W), Deposit money (D), or Check your balance (B)?")

    # Capitalize the user input
    userChoice = userChoice.capitalize()

    # If the user chooses to withdrawal
    if userChoice == 'W':

        # Get user input for which account to withdrawal money from
        accountChoice = input(
            "Would you like to withdrawal from your Checking (C) or your Savings (S)?")

        # Capitalize the choice that was made
        accountChoice = accountChoice.capitalize()

        # If the user selects checking
        if accountChoice == 'C':

            # Create a userCheckingAccount veriable and assign it to the main CheckingAccount class
            userCheckingAccount = CheckingAccount(
                accountNumber, BIG_ACCOUNT_AMOUNT)

            # Call the withdrawl function inside of the CheckingAccount class
            userCheckingAccount.withdrawl()

        # If the user selects Savings
        elif accountChoice == 'S':

            # Create a userSavings variable and assign it to the SavingsAccount class
            userSavings = SavingsAccount(accountNumber, BIG_ACCOUNT_AMOUNT)

            # Call the withdrawl method using the userSavings variable
            userSavings.withdrawl()

            # Call the addInterest method using the userSavings variable
            userSavings.addInterest()

        # If the user did not select checking or savings, shut down the program
        else:
            print("User did not choose Checking or Savings, shutting down...")

    # If the user selected deposit
    elif userChoice == 'D':

        # Get user input for which account to deposit money into
        accountChoice = input(
            "Would you like to deposit into your Checking (C) or your Savings (S)?")

        # Capitalize the choice that was made
        accountChoice = accountChoice.capitalize()

        # If the user selected checking
        if accountChoice == 'C':

            # Create a userCheckingAccount veriable and assign it to the main CheckingAccount class
            userCheckingAccount = CheckingAccount(
                accountNumber, BIG_ACCOUNT_AMOUNT)

            # Call the deposit method with the userCheckingAccount variable
            userCheckingAccount.deposit()

        # If the user chose Savings
        elif accountChoice == 'S':

            # Create a userSavings variable and assign it to the SavingsAccount class
            userSavings = SavingsAccount(accountNumber, BIG_ACCOUNT_AMOUNT)

            # Call the deposit method using the userSavings variable
            userSavings.deposit()

            # Call the addInterest method using the userSavings variable
            userSavings.addInterest()

        # If the user did not select checking or savings, shut down the program
        else:

            print("User did not choose checking or savings, shutting down....")

    # If the user chose check balance
    elif userChoice == 'B':

        # Get user input for which account to chheck the balance for
        accountChoice = input(
            "Would you like to Check the balance of your Checking (C) or your Savings (S)?")

        # Capitalize the choice that was made
        accountChoice = accountChoice.capitalize()

        if accountChoice == 'C':

            # Create a userCheckingAccount veriable and assign it to the main CheckingAccount class
            userCheckingAccount = CheckingAccount(
                accountNumber, BIG_ACCOUNT_AMOUNT)

            # Call the getBalance method with the userCheckingAccount variable
            userCheckingAccount.getBalance()

        elif accountChoice == 'S':

            # Create a userSavings variable and assign it to the SavingsAccount class
            userSavings = SavingsAccount(accountNumber, BIG_ACCOUNT_AMOUNT)

            # Call the getBalance method using the userSavings variable
            userSavings.getBalance()

            # Call the addInterest method using the userSavings variable
            userSavings.addInterest()

        # If the user did not select checking or savings, shut down the program
        else:

            print("User did not choose checking or savings, shutting down....")

    # This is for the error if the user does not type in a 'W' for Withdrawl, 'D' for Deposit, or 'B' for Check Balance
    else:
        print("Please only enter in 'W' for Withdraw, 'D' for Deposit, or 'B' for Balance")

        # If the user makes this error, rerun the big_account method
        big_account(accountNumber)

# Create a function to run the small account


def small_account(accountNumber):

    # Create a checking account variable and set it to the CheckingAccount class
    userChecking = CheckingAccount(accountNumber, SMALL_ACCOUNT_AMOUNT)

    # Call the checkMinimumBalance function
    userChecking.checkMinimumBalance()

    # Get user input for the user choice to ask them if they would like to
    # Withdrawl, deposit,, or check balance
    userChoice = input(
        "Welcome to your account. Would you like to Withdrawl (W), Deposit money (D), or Check your balance (B)?")

    # Capitalize the user input
    userChoice = userChoice.capitalize()

    # If the user chooses to withdrawal
    if userChoice == 'W':

        # Get user input for which account to withdrawal money from
        accountChoice = input(
            "Would you like to withdrawal from your Checking (C) or your Savings (S)?")

        # Capitalize the choice that was made
        accountChoice = accountChoice.capitalize()

        # If the user selects checking
        if accountChoice == 'C':

            # Create a userCheckingAccount veriable and assign it to the main CheckingAccount class
            userCheckingAccount = CheckingAccount(
                accountNumber, SMALL_ACCOUNT_AMOUNT)

            # Call the withdrawl function inside of the CheckingAccount class
            userCheckingAccount.withdrawl()

        # If the user selects Savings
        elif accountChoice == 'S':

            # Create a userSavings variable and assign it to the SavingsAccount class
            userSavings = SavingsAccount(accountNumber, SMALL_ACCOUNT_AMOUNT)

            # Call the withdrawl method using the userSavings variable
            userSavings.withdrawl()

            # Call the addInterest method using the userSavings variable
            userSavings.addInterest()

        # If the user did not select checking or savings, shut down the program
        else:
            print("User did not choose Checking or Savings, shutting down...")

    # If the user selected deposit
    elif userChoice == 'D':

        # Get user input for which account to deposit money into
        accountChoice = input(
            "Would you like to deposit into your Checking (C) or your Savings (S)?")

        # Capitalize the choice that was made
        accountChoice = accountChoice.capitalize()

        # If the user selected checking
        if accountChoice == 'C':

            # Create a userCheckingAccount veriable and assign it to the main CheckingAccount class
            userCheckingAccount = CheckingAccount(
                accountNumber, SMALL_ACCOUNT_AMOUNT)

            # Call the deposit method with the userCheckingAccount variable
            userCheckingAccount.deposit()

        # If the user chose Savings
        elif accountChoice == 'S':

            # Create a userSavings variable and assign it to the SavingsAccount class
            userSavings = SavingsAccount(accountNumber, SMALL_ACCOUNT_AMOUNT)

            # Call the deposit method using the userSavings variable
            userSavings.deposit()

            # Call the addInterest method using the userSavings variable
            userSavings.addInterest()

        # If the user did not select checking or savings, shut down the program
        else:

            print("User did not choose checking or savings, shutting down....")

    # If the user chose check balance
    elif userChoice == 'B':

        # Get user input for which account to chheck the balance for
        accountChoice = input(
            "Would you like to Check the balance of your Checking (C) or your Savings (S)?")

        # Capitalize the choice that was made
        accountChoice = accountChoice.capitalize()

        if accountChoice == 'C':

            # Create a userCheckingAccount veriable and assign it to the main CheckingAccount class
            userCheckingAccount = CheckingAccount(
                accountNumber, SMALL_ACCOUNT_AMOUNT)

            # Call the getBalance method with the userCheckingAccount variable
            userCheckingAccount.getBalance()

        elif accountChoice == 'S':

            # Create a userSavings variable and assign it to the SavingsAccount class
            userSavings = SavingsAccount(accountNumber, SMALL_ACCOUNT_AMOUNT)

            # Call the getBalance method using the userSavings variable
            userSavings.getBalance()

            # Call the addInterest method using the userSavings variable
            userSavings.addInterest()

        # If the user did not select checking or savings, shut down the program
        else:

            print("User did not choose checking or savings, shutting down....")

    # This is for the error if the user does not type in a 'W' for Withdrawl, 'D' for Deposit, or 'B' for Check Balance
    else:
        print("Please only enter in 'W' for Withdraw, 'D' for Deposit, or 'B' for Balance")

        # If the user makes this error, rerun the big_account method
        small_account(accountNumber)


# Create a function to run the program
def runProgram():

    # Use try/except to make sure the user only inputs numbers for the account number
    try:
        accountNumber = float(input(
            "(20202 - Big Account)   (10101 - Small Account)\nPlease enter the account number for which account you would like to view: "))

    # If the user enters in non-numbers, prompt them and re-run the runProgram method
    except:
        print("Please only type in numbers!")

        # Re-run the method
        runProgram()

    # If the account number that was entered == the big account number
    if accountNumber == BIG_ACCOUNT_NUMBER:

        # Call the big_account funtion with the account number that was given
        big_account(accountNumber)

    # Else if, the account number == the small account number
    elif accountNumber == SMALL_ACCOUNT_NUMBER:

        # Call the small_account function with the account number that was given
        small_account(accountNumber)

    # If the account number does not match any accounts, prompt the user and re-run the runProgram method
    else:
        print("Could not find account. Try again!")

        # Run the runProgram method
        runProgram()

# Create a runAgain function to ask the user if they would like to continue running the program


def runAgain():

    # Get user input if they would like to run the program again
    userChoice = input("Would you to run again? Yes (Y) or No (N) ")

    # Capitalize the input that was given
    userChoice = userChoice.capitalize()

    # If the user typed in a 'Y' for yes
    if userChoice == 'Y':

        # Call the runProgram function to restart the program
        runProgram()

    # If the user typed in an 'N' for no
    elif userChoice == 'N':

        # Quit the application
        quit()

        # This was for testing as I was getting an error
        # and needed to see if the application was even reaching this point
        # I didn't know if the issue was the quit() function I used
        print("Quitting")

    # If the user did not type in a 'Y' for Yes or 'N" for No, prompt them and rerun the runAgain function
    else:
        print("Please only use 'Y' for Yes or 'N' for No")

        # Run the runAgain function
        runAgain()


# This is to start the program.
# It calls the runProgram function
runProgram()
