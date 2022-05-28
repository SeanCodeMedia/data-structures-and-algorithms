

def find_first_one(arr):
	for i in range(len(arr)):
		if arr[i] == 1:
			return i
	return -1


print(find_first_one([0, 0, 0, 1, 1, 1, 1, 1]))