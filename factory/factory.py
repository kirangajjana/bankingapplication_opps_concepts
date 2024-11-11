from app import Account
from deposit import Deposit
from registration import Registration
from withdraw import Withdraw

class Bank:
    def create_account():
        return Account()
    def create_deposit():
        return Deposit
    def create_withdraw():
        return Withdraw()
    def create_registration(name,city):
        return Registration(name,city)