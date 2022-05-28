class Node:
    
    data = None
    next_node = None

    def __init__(self, data):
    	self.data = data


class LinkList:

	def __init__(self):
		self.head = None


	def size(self):

		node_count = 0 

		current = self.head

		while current:

			node_count += 1

			current = current.next_node 

		return node_count


	def add(self, data):
		'''
		add a node to the head of the link List
		''' 
		new_node = Node(data)
		new_node.next_node = self.head 
		self.head = new_node


	def get_head(self):
		return self.head

	def remove(self, key): 

		current = self.head
		previous = None 

		if key is self.head.data: 
			self.head = self.head.next_node

		else:
			while current:

				if current.data  == key:

					current = previous
					current.next_node = previous.next_node.next_node 

					return 1

				previous = current
				current  = current.next_node
			



	def remove_at_index(self, index):

		current = self.head

		count = 0 

		if index >  self.size():
			print("Error: out of bound sorry")
			return -1

		while count < index-1 and current:

			count += 1
			current = current.next_node

		current.next_node = current.next_node.next_node

	def print_nodes(self):
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


	def __repr__(self):
		self.print_nodes()


ll = LinkList()
ll.add(1)
ll.add(3)
ll.add(7)

l2 = LinkList()
l2.add(1)
l2.add(2)

head1 = ll.get_head()
head2 = l2.get_head()

result = Node(0)

data = []

while head1 and head2:


    if head1.data <= head2.data:
    	data.append(head1.data)
    	head1 = head1.next_node

    elif head1.data > head2.data:
    	data.append(head2.data)
    	head2 = head2.next_node

    	
    	#print(result.data)

    #result = result.next_node

print(data)

   
    








