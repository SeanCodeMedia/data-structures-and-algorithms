
class Item:
	pay_rate = 0.8 # class attrubutes 
	def __init__(self, name:str, price:float, quantity=0):
		
		# validation
		assert price >= 0,    f"Price {price} is not greater than zero!" 
		assert quantity >= 0, f"Price {quantity} is not greater than zero!" 

		self.name = name  # instance attributes
		self.price = price
		self.quantity = quantity
	
	def calcualte_total_price(self):
		return self.price * self.quantity






item1 = Item("phone", 100, 10)
print(item1.pay_rate)
print(item1.calcualte_total_price())

item2 = Item("laptop", 200, 20)
print(item2.calcualte_total_price())


# item2 = Item()
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.calcualte_total_price(item2.price, item2.quantity))

