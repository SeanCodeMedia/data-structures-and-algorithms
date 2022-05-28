class Car:

	def __init__(self):
		pass 

	def start_engine(self):
		print("turn on")
		return self

	def turn_off_engine(self):
		print('turn off')
		return self

	def drive(self):
		print("drive")
		return self 

	def park(self):
		print("park car")
		return self

	def stop(self):
		print("foot on the break")
		return self


car_one = Car()
car_one.start_engine().drive().stop().park().turn_off_engine()


my_dic = {(1,2): "cat", 2: "rat", 3:"mat", 4: "sat"}

print(my_dic[(1,2)])