
def find_duplicates(arr1, arr2):

	over_lapping_values = []

	if len(arr1) >= len(arr2):
		for number in arr1:
			if number in arr2:
				over_lapping_values.append(number)
	else: 
		for number in arr1:
			if number in arr2: 
				over_lapping_values.append(number)

	return over_lapping_values
	

print(find_duplicates([3, 6, 7, 8, 20], [1, 2, 3, 5, 6, 7]))