"""Withdrawal Dialog."""

import sys
import questionary


def make_withdrawal(account):
    """Adjusts account balance for withdrawl.

        Script that verifies withdrawl amount is valid and adjusts account balance.

        Arg:
            account(dict): contains pin and balance for account

        Return:
            account(dict): returns account with balance adjusted for deposit

    """

    # @TODO:  Use questionary to capture the withdrawal and set it equal to amount variable. Be sure that amount is a floating point number.
    amount = questionary.text("How much would you like to withdrawl?").ask()
    amount = float(amount)
    print(amount)

    # @TODO:  Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if amount <= 0:
        sys.exit("Not a valid withdrawl amount. Exiting.")
    
    # @TODO: Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"WITHDRAWL CONFIRMATION: ${amount}")
        return account
    else:
        sys.exit("Insufficient funds for withdrawl. Exiting.")
    
