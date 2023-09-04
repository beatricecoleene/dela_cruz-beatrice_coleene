class Convinience_store:
	store=" "
	def enter_store(self, store):
		print(f"Customer entered to {store}")
		

class Basket:
	
	def __init__(self):
		print("Customer picked up a basket")
		
class Product:
		def __init__(self, kind_of_product, brand, flavor, how_many, price):
			self.kind_of_product=kind_of_product
			self.brand=brand
			self.flavor=flavor
			self.how_many=how_many
			self.price=price
		def product(self):
			print(f"Customer choose {self.brand} {self.kind_of_product} {self.flavor}")
			

		
bs= Basket		
cs= Convinience_store()
product= Product("Slurpee", "7/11", "Strawberry ", 1, 35)
cs.enter_store("Seven-Eleven")
bs()
product.product()