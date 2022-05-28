# def a():
# 	return "hey " + b()


# def b():
# 	return "Sean" + c()


# def c():
# 	return "!"

# print(a())

# Recursion with strings 

# def reverse_string(input):

# 	if input == "": # base case
# 		return input
# 	count = 0
# 	return reverse_string(input[count+1:]) + input[count] 


# #print(reverse_string("Hello"))


# #ello  

# remove  = False

# def is_paliondrone(input): # global recursion

# 	global remove

# 	length = len(input)-1 
# 	counter = 0

# 	# base case 
# 	if input == "" or len(input) == 1:
# 		return True 

# 	# break drown the problem here by one step

# 	if input[counter] == input[length]: 
# 		return is_paliondrone(input[counter+2:length-1])
# 	elif input[counter] != input[length] and remove == False:
# 		remove = True
# 		return is_paliondrone(input[counter+2:length-2])
# 	return False

# print(is_paliondrone("racecar"))


# def is_paliondrone(input,remove): # threading

# 	length = len(input)-1 
# 	counter = 0

# 	# base case 
# 	if input == "" or len(input) == 1:
# 		return True 

# 	# break drown the problem here by one step

# 	if input[counter] == input[length]: 
# 		return is_paliondrone(input[counter+2:length-1],False)
# 	elif input[counter] != input[length] and remove == False:
# 		return is_paliondrone(input[counter+2:length-2],True)
# 	return False

# print(is_paliondrone("racecars",False))


# def is_paliondrone(input): # threading

# 	length = len(input)-1 
# 	counter = 0

# 	# base case 
# 	if input == "" or len(input) == 1:
# 		return True 

# 	# break drown the problem here by one step

# 	if input[counter] == input[length]: 
# 		return is_paliondrone(input[counter+2:length-1])

# 	return False

# print(is_paliondrone("racecar"))


# 1+2+3+4....

# def sub(count):

# 	if count == 0:
# 		return

# 	print(count)
# 	sub(count-1)

# sub(10)


# def decimal_to_binary(num, result):

# 	if num == 0: # base case
# 		return result

# 	result = str(num%2) + result

# 	return decimal_to_binary(num//2,result)

# print(decimal_to_binary(5,""))


# def sum_natural_numbers(num, counter, num_sum):

# 	if counter == num+1: 
# 		return num_sum

# 	# breaking the problem down
# 	return sum_natural_numbers(num, counter+1, num_sum+counter)

# print(sum_natural_numbers(10,0,0))


# def factorial(num): 

# 	if num == 1 or num == 0: 
# 		return num

# 	return num*factorial(num-1)

# print(factorial(5))


# binary seeach

#
# num = [1, 10, 25, 50, 75, 100]
#
# # []

# def binary_search(item):
#
# 	start = 0
#
# 	end = len(num)-1
#
# 	while  start <= end:
#
# 		mid_point = (start + end) // 2
#
# 		print(mid_point)
#
# 		if  num[mid_point] == item:
# 			return True
#
# 		elif num[mid_point] < item:
#
# 			start = mid_point + 1
#
# 			print(num[start:])
#
# 		elif num[mid_point] > item:
#
# 			end = mid_point - 1
#
# 			print(num[:end])
#
# 	return False
#
#
# #print(binary_search(9))

# OLog(N)
# def binary_search_recursion(item, num_list):
# 	if len(num_list) == 0:
# 		return False
# 	else:
# 		mid_point = (len(num_list) - 1) // 2
# 		if num_list[mid_point] == item:
# 			return True
# 		elif num_list[mid_point] < item:
# 			num_list = num_list[mid_point + 1:]
# 			return binary_search_recursion(item, num_list)
# 		elif num_list[mid_point] > item:
# 			num_list = num_list[:mid_point]
# 			return binary_search_recursion(item, num_list)
# 	return False
#
#
# print(binary_search_recursion(10, num))


#
# def binary_search_recursion_2(item, start, end): # in place
#
# 	mid_point = (start+end) // 2
#
# 	if mid_point == len(num): # input has to be ordered
# 	 		return False
#
# 	if num[mid_point] == item:
# 		return True
# 	if num[mid_point] < item:
# 		return binary_search_recursion_2(item, mid_point+1, end)
# 	elif num[mid_point] > item:
# 		return binary_search_recursion_2(item, start, mid_point-1)
# 	return False
#
#
# print(binary_search_recursion_2(1000, 0, len(num)-1))

# def fib(n):
#     if n == 1 or n == 0:
#         return n
#     return fib(n-1) + fib(n-2)
#
#
# print(fib(10))


unsorted = [1, -1, 3, 6, 7, 8, 2, 5, 8]


def merge_sort(start, end):

	if start <= end:
		return "Done"

	mid_point = (start+end)//2
	print(mid_point)
	# merge_sort(start, mid_point+1)
	# merge_sort(mid_point, end)


merge_sort(0, 100)