
class Animal:

	alive = True

	def eat(self):
		print("I can eat")

	def sleep(self):
		print("I can sleep")



class Rabbit(Animal):

	def run(self):
		print("I run")

class Fish(Animal):

	def swim(self):
		print("I can swim")


class Hawk(Animal):

	def fly(self):
		print("I can fly")




rabbit_1 = Rabbit()
rabbit_1.eat()
rabbit_1.sleep()
rabbit_1.run()