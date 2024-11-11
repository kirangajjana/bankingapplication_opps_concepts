from app import Account as kiran
class Registration:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        pass
    def info(self):
        print(f"welcome to {kiran.bank_name}")
        print(f"hello mr. {self.name}")
        print(f"your are from city {self.city}")
name=input("please enter your name")
city=input("please enter your city")
b=Registration(name,city)     
b.info()   