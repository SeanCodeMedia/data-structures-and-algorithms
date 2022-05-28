

def linear_search(a, target) -> None: 
	'''
	return index if element is found None if not found
	'''

	for x in range(len(a)): 
		if a[x] == target: 
			return x 
	return None


myList = list(range(1,100000000))
print(linear_search(myList, 10000000)) 