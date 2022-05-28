
# link list is better at delete and inserting values O(1)
# A link list is a linear DataStucture we each element in a list is a object call a node 
#  the node has two data values 1) a pointer that points to a Node and value
#  first node is called the Head the last node is called the tail Denote the end of the 
# list and point to null or None 

# single link list


class Node(object):

	'''
	object for storing a single node of a link list
	data:
	next_node: 
	'''

	data = None
	next_node = None

	def __init__(self, data): 
		self.data = data

	def __repr__(self):
		return "<Node data> {self.data}"


class LinkList: 

	'''
	Singly Linked List 
	'''

	def __init__(self):
		self.head = None 

	def is_empty(self):
		return self.head == None 

	def size(self): 
		'''
		return the number of node in a linked list takes 
		Linear time O(N)
		'''
		current = self.head 
		count = 0 
		while current: 
			count += 1 
			current = current.next_node
		return count 

	def add(self, data):
		'''
		adds a new Node containing data at the head of the list
		'''
		new_node = Node(data)
		new_node.next_node = self.head
		self.head = new_node

	def search(self, key):
		'''
		search the link list for the first node that matches the data and 
		return true when is found otherwise it will return false if not in the 
		link list this operation runs at O(N)t O(1)s
		'''
		current_node = self.head

		while current_node:
			if current_node.data is key:
				return True
			current_node = current_node.next_node

		return False

	def __repr__(self):
		current = self.head
		nodes = []

		while current:
			if current is self.head:
				nodes.append("[Head is %s]" % current.data)
			elif current.next_node is None:
				nodes.append("Tail: %s" % current.data)
			else:
			    nodes.append("%s" % current.data)

			current = current.next_node 
		return "->".join(nodes)

	def insert(self, index, data): 

		current_node = self.head
		position = 0

		if index > self.size():
			print("out of index cannot insert")
			return - 1

		while current_node: 
			# 	'''
			# 	runs in O(N) time because we might have to run through entire list to insert
			# 	insert is O(1)
			#   trick is to get the node before the node we want to insert at and 
			#   store this node in a var call previous node 
			#   this node will contain the properties we need to insert 
			# 	'''
			if index == 0:
				self.add(data)
				return index

			while position+1 != index:
				position += 1 
				current_node = current_node.next_node

			# better var names might clear this up
			previous_node = current_node
			current_next_node = current_node.next_node

			new_node = Node(data)
			previous_node.next_node = new_node
			new_node.next_node = current_next_node

			return index


	def remove(self, key):
		# look over this function
		current_node = self.head

		previous_node = None

		is_Found = False

		while current_node and not is_Found:

			if current_node.data == key and current_node == self.head:
				is_Found = True
				self.head = current_node.next_node
				

			elif current_node.data == key:
				is_Found = True
				previous_node.next_node = current_node.next_node # key here
			

			else:
				previous_node = current_node # the key here 
				current_node = current_node.next_node
		return current_node

	def remove_at_index(self, index):

		'''
		review this code please :) 
		'''

		if index > self.size():
			print("sorry out of bound")
			return -1

		position = 0
		current_node = self.head

		while position+1 != index and current_node: # stop before we hit index
			position =+1
			current_node.next_node

		previous_node = current_node
		
		if current_node.next_node == None:
			previous_node.next_node = None 
		else:
			current_node = current_node.next_node
			previous_node.next_node = current_node.next_node 
		return current_node










			













