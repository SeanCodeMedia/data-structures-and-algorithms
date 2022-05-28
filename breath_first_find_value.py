class Node:

	def __init__(self, data):
		self.data = data
		self.left = None 
		self.right = None



class Queue: 

	def __init__(self):
		self.queue = [] 

	def dequeue(self): 
		value = self.queue.pop(0)
		return value


	def enqueue(self, item): 
		self.queue.append(item)

	def peek(self):
		return self.queue[len(self.queue)-1]

	def is_empty(self):
		if len(self.queue) > 0: 
			return False 
		if len(self.queue) == 0:
			return True



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 


my_queue = Queue()



def breath_first_find(root, key):

	my_queue.enqueue(root)

	while not my_queue.is_empty():

		current = my_queue.dequeue()

		if current.data == key: 
			return True

		if current.left:
			my_queue.enqueue(current.left)

		if current.right: 
			my_queue.enqueue(current.right)

	return False



print(breath_first_find(a, "c"))




