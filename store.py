class Person:
    def __init__(self,name):
        self.name=name
class Wallet:
    def cash(self, cash):
        self.cash=cash

class Basket:
    def __str__(self,size):
        size=" "
        print(f"The basket you picked is {size}")
    

class Shelf:
    def products(self,product):
        self.products=products




if __name__=='__main__':
    basket=Basket("mediuim")