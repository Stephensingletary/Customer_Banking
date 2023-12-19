# Import the create_cd_account and create_savings_account functions
from Account import Account
from savings_account import create_savings_account 
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = input("Set initial savings balance: ")
    savings_interest = input("Set interest rate: ")
    savings_maturity = input("Set number of months for savings to mature: ")

    # Call the create_savings_account function and pass the variables from the user.
    savings_account = Account(float(savings_balance), float(savings_interest), int(savings_maturity))
    savings_account.create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print()

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input("Set the initial CD balance: ")
    cd_interest = input("Set the interest rate: ")
    cd_maturity = input("Set the number of months for CD to mature: ")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print([updated_cd_balance, interest_earned])

if __name__ == "__main__":
    # Call the main function.
    main()