
# Java and C++ arrays are Homogeneous containers  Meaning that you can only store one data
# type with in the array 
# python however has heterogenous structures (array)/List 
#which can store mix data types such as 
# int float ect ... 
# arrays are contiguious memory and stored next to each other in memory with no gaps 
# a bit is 8 bits makes a byte 
# 64 bit numbers takes up 8 memeory blocks  2^8 = 64 
# 32 bit numbers takes up 4 memeory blocks  2^4 = 32 
# for example if we store a bit int we take up something like this 
# if each slot is 8 bytes (not bit) in this example
#[1,2,3,4,5]
# ==========================
#|*|*|*|*|*||||||||||||||| back to back memory slots 
#|||||||||||||||||||||||||
#|||||||||||||||||||||||||


new_list = [1,2,3,6]

result = new_list[0]

print(result) 


