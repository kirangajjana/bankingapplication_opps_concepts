# main.py

from factory.factory import Bank

# Creating instances through the factory
account_instance = Bank.create_account()
deposit_instance = Bank.create_deposit()
registration_instance = Bank.create_registration()
withdraw_instance = Bank.create_withdraw()

# Use the created instances as needed
account_instance.name1()       # Example method in Account
deposit_instance.some_method()       # Example method in Deposit
registration_instance.some_method()  # Example method in Registration
withdraw_instance.some_method()      # Example method in Withdraw
