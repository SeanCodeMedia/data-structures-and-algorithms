
# a string is a orded and immutable data type and text representation 

from timeit import default_timer as timer

my_string = "Hello My Friend"

print(my_string)

# multi line string 

my_string_muli = """ 
Kenzie Academy and \
Amazon Technical Academy\
co-developed this online
Software Engineering with 
Specialization in Backend 
Java program for growth-minded learners\
"""

print(my_string_muli)


# accssing chars 

char = my_string[-2]
print(char)


# cannot change a character at index :O :) 
#char[0] = "K"
#print(char)

# strings in python cannot be changed they are static 

# ----------------------------- slicing 
print(my_string[:5])

# reverse a string

print(my_string[::-1]) # very fast why to reverse a list :)


print(my_string[::2])  # step counter

# ----------------------concatincation of strings 

first = "sean "

last = "peart"

name = first + last 

print(name)

# ----------------looping over strings------

for x in first:
	print(x)

# # or 

# for x in range(len(first)): 
# 	print(first[x])



# check if something in string


if "s" in first: 
	print("yes")
else: 
	print("no")


# or check for substrings 

if "sea" in first: 
	print("yes")
else: 
	print("no")

if "sean P" in first: 
	print("yes")
else: 
	print("no")


# removing white spaces 


my_string_1 = "        big brown cat           "
print(my_string_1)

# strip
my_string_1 = my_string_1.strip() # it does not change string in place it will make a copy
print(my_string_1)

# changing cases 

upper = my_string_1.upper() # does not change in place as well
print(upper)


lower = my_string_1.lower() # does not change in place as well
print(lower)


#  check if string starts with 

print(my_string_1.startswith("b"))
print(my_string_1.startswith("B"))
print(my_string_1.startswith("H"))

# check if string ends with 

print(my_string_1.endswith("t"))
print(my_string_1.endswith("c"))


# find 
print(my_string_1.find("c")) #return the index

# count 
print(my_string_1.count("c"))

print(my_string_1.count("k"))


# replace 

# will return a new string 
my_string_2 = my_string_1.replace("cat", "dog")
print(my_string_2)


# list and strings 
# covert a string to a list
my_string_3  = "hey my frend"
my_list = my_string_3.split(" ") # use space as dilimiter
print(my_list)


my_string_4  = "hey,my,frend"
my_list_2 = my_string_3.split(",") # use space as dilimiter
print(my_list)


#------------------ join method 
# very useful method
sentence = "".join(my_string_4)
print(sentence)


my_list = ['a'] * 100

#print(my_list)

# if we want to turn my_list into a string
# bad code 
# becuse we keep creating a
# new string in python
# start = timer()
# my_string = ''
# for x in my_list: 
# 	my_string += x
# print(my_string)
# stop = timer()
# print(stop-start)
# instead do this
# good
my_string = ''
print(my_string.join(my_list))


# =========format strings =====================

#old way of doing it 


my_name = "sean "
my_new_string = "%sis going to the park" % my_name
print(my_new_string)

my_name = 43
my_new_string = "%d is going to the park" % my_name
print(my_new_string)


my_name = 1.224
my_new_string = "%f is going to the park" % my_name
print(my_new_string)

# new way of doing things

my_name = "sean "
my_new_string = "{} is going to the park".format(my_name)
print(my_new_string)


num  = 1.233
num_2 = 1.35123
my_new_string = " number is {:.2f} and {}".format(num, num_2)
print(my_new_string)

# f string 
# this the way to go 
var_num = 123
var = f"my number is {var_num}"

print(var)

# filter 

