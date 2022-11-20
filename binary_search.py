'''
O(N)
linear search
Big O is order of magnitued of complexity 
measure complexity as the input size grow 
O Log(N)
binary seach 
Reading value in a list is contstant time O(1)
Inverse of a exponent is a Logarithm 
log2 of N + 1 
log2(n+1)
for example 
log is sublinear 
------
log2(8)  = 3 because 2^3 = 8 
log2(16) = 4 becuase 2^16 = 4 
Polynomial runtime 
N^K  
'''


# [1,2,3,4,5,6,7,8,9,10]
# Binary search list has to be sorted 
def binary_search(my_list, target):
    start_index = 0
    end_index = len(my_list) - 1

    while start_index <= end_index:
        mid_point = (start_index + end_index) // 2  # key to binary search ---
        # this is my solution did not work :( But make sense
        if my_list[mid_point] == target:
            return mid_point
        elif my_list[mid_point] < target:
            start_index = mid_point + 1
        else:
            end_index = mid_point - 1

    return None


# current_index  - len
# [1,2,3,4,5,6]
# [4,5,6]
# [6]

myList = list(range(1, 10))

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5))
