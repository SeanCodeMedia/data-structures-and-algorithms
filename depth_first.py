
class Node:

	def __init__(self, data):
		self.data = data
		self.left = None 
		self.right = None


class stack:

	def __init__(self):
		self.stack = []


	def push(self, item):
		self.stack.insert(0, item)

	def pop(self):
		value = self.stack.pop(0)
		return value


	def peek(self):
		return self.stack[0]


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

# iterative soultion
def depth_first_triversal(root):
	
	my_stack.push(root)

	while not my_stack.is_empty():

		current = my_stack.pop()
		print(current.data)

		if current.right:
			my_stack.push(current.right) # explore the right side of the tree first
		if current.left:
			my_stack.push(current.left) # then we move across the tree
	

depth_first_triversal(a)



# recursive solution

# def depth_first(root):

# 	if root == None:
# 		return [] 

# 	left  =  depth_first(root.left) #    [b, d, e]

# 	right =  depth_first(root.right) #  [c, f]

# 	return [root.data, left, right] # would need to unpack array



# print(depth_first(a))
