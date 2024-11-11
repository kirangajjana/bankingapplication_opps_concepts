# main.py

from factory.factory import Bank

# Creating instances through the factory
account_instance = Bank.create_account()
deposit_instance = Bank.create_deposit()
registration_instance = Bank.create_registration("hyd","cyd")
withdraw_instance = Bank.create_withdraw()

# Use the created instances as needed
    # Example method in Withdraw
