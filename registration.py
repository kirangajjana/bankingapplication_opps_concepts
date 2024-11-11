from app import Account as kiran
class Registration:
    def __init__(self,name,city): #instance method
        self.name=name #instance variable
        self.city=city
        kiran.transcation+=1
        pass
    def info(self):
        print(f"welcome to {kiran.bank_name}")
        print(f"hello mr. {self.name}")
        print(f"your are from city {self.city}")
name=input("please enter your name")
city=input("please enter your city")
b=Registration(name,city)     #object creation
b.info()   