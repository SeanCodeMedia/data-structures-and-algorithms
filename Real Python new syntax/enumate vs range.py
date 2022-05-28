
array = [10, 27, 8, 9,10, 25]

def frizz_buzz(list:array) -> list:
	# for x in range(len(array)):
	# 	if array[x] % 2 == 0: 
	# 		array[x] = "frizz"
	# 	elif array[x] % 5 == 0: 
	# 		array[x] = "buzz"
	# return array
    
    # for x, i in enumerate(array):
    # 	if i%2 == 0:
    # 		array[x] = "frizz"
    # 	elif i % 5 == 0:
    # 		array[x] = "buzz"
    # return array

    for x, i in enumerate(array):
    	if i%2 == 0:
    		array[x] = "frizz"
    	elif i % 5 == 0:
    		array[x] = "buzz"
    return array

print(frizz_buzz(array))




