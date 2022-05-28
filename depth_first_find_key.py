
class Node:

	def __init__(self, data):
		self.data = data
		self.left = None 
		self.right = None


class stack:

	def __init__(self):
		self.stack = []


	def push(self, item):
		# treat the end of list as the head of the stack so we get almost O(1)
		self.stack.append(item)

	def pop(self):
		value = self.stack.pop(len(self.stack)-1)
		return value


	def peek(self):
		return self.my_stack[len(self.stack)-1]


	def is_empty(self): 

		if len(self.stack) > 0: 
			return False 
		else: 
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


my_stack = stack()

#O(N)
def find_value_in_tree(root, key): 

	my_stack.push(root)

	while not my_stack.is_empty(): 

		current = my_stack.pop()

		if current.data == key: 
			return True

		if current.right:
			my_stack.push(current.right)

		if current.left: 
			my_stack.push(current.left)

	return False 

print(find_value_in_tree(a, "d"))