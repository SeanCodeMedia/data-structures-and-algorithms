def sortedSquaredArray(array):
    squaredArray = [ 0 for _ in array]
    low = 0
    high = len(squaredArray)
	
	for x in reversed(range(len(squaredArray))):
		
		low_squared = abs(array[low]) ** 2 
		high_squared  = abs(array[high-1]) ** 2 
		
		if low_squared > high_squared: 
			squaredArray[x] = low_squared
			low += 1
		else:
			squaredArray[x] = high_squared
			high += 1