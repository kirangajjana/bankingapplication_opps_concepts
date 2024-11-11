from app import Account
class Withdraw:
    def __init__(self):
        print(f"welcome to {Account.bank_name}")
        Account.transcation+=1
a=Withdraw()        