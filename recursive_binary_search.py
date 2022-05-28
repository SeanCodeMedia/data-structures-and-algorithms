

def recursive_binary_search(myList, target): 
	# uses more memory 
	# run time O(Log(N)) Space time is also O(Log(N))  
	# need less space because every function call we use less memory 
	#  when you call recursive function will break the problem down in every step 
	
	#base case 
	if len(myList) == 0:
		return False 
	else: 
		mid_point = (len(myList)) //2 

		if myList[mid_point] == target: 
			return True 
		else: 
			if myList[mid_point] < target:
				return recursive_binary_search(myList[mid_point+1:], target)
			else: 
				myList[mid_point] < target
				return recursive_binary_search(myList[:mid_point-1], target)


print(recursive_binary_search([1,2,3,4,5,6], 1))
