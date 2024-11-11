from app import Account
from deposit import Deposit
from registration import Registration
from withdraw import Withdraw

class Bank:
    def create_account(self):
        return Account()
    def create_depoit(self):
        return Deposit
    def create_withdraw(self):
        return Withdraw()
    def create_registration(self):
        return Registration()