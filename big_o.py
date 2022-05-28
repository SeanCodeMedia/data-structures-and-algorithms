

# def add_one_to_first_in_element(num): 
# 	total = num[0] + 1 
# 	print(total)

# add_one_to_first_in_element([2,3,5])




# def add_sum (num):

# 	sum = 0

# 	for index in range(len(num)): 

# 		sum = sum + num[index]

# 	return sum


# print(add_sum([1,2,3,4]))



def pair_value_together(num):

	pair_list  = []

	for index in range(len(num)):

		pair_list.append(num[index])

		for index in range(len(num)):

			pair_list.append(num[index])


	return pair_list


#print(pair_value_together(list(range(8000))))


# def pair_value_together_2(num):

# 	pair_list  = []

# 	for index in range(len(num)):
# 		pair_list.append(num[index])
# 		pair_list.append(num[index])


# 	return pair_list

# print(pair_value_together_2([1,2,3,4]))






