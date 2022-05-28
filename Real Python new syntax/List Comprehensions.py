
def moveElementToEnd(array, toMove):
	i = 0
	j= len(array)-1
	
	while i < j: 
		if  array[i] == toMove  and array[j] == toMove: 
			j-= 1 
		elif  array[i] == toMove and array[j] != toMove:
			array[i],array[j] = array[j], array[i]
			i+=1
			j-=1
		elif array[i] != toMove and  array[j] != toMove:
			i+=1
			
	return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))