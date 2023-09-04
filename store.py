class Convinience_store:
    store= " "
    def enter_store(self,store):
        print(f"Costumer entered  {store}")

class Basket:
    def basket(self):
        print("Customer picked up a basket") 
class Product:
    def __init__(self,kind_of_product, brand, flavor, how_many, price):
        self.kind_of_product= kind_of_product
        self.brand= brand
        self.flavor= flavor
        self.how_many= how_many
        self.price=price
    def product(self):
        print(f"Customer choose {self.brand} {self.kind_of_product} {self.flavor}")

class Cashier:
    pass

class Wallet:
    def cash(self, cash):
        self.cash=cash

basket= Basket()
cs= Convinience_store()
csh= Wallet() 
prod= Product("Slurpee", "7/11", "Strawberry ", 1, 35)
cs.enter_store("Eleven-Seven")
basket.basket()
prod.product()
csh.cash(100)