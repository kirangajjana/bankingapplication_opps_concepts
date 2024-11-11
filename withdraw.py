from app import Account
class Withdraw:
    def __init__(self): #instance method
        print(f"welcome to {Account.bank_name}") 
        Account.transcation+=1 #transactions to know about the total number of transactions we have done at the end
a=Withdraw()        