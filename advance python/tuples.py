# a tuple is a collection data type that is orderd and static or imputable
# cannot be changed after being created 

# something new I didn't learn 

# if you have one element is ("max")
my_tuple = ("Max")
print(type(my_tuple))
# if you create a tuple with
# just a string it will retrun a tpye
# str 
# same for a int or float
my_tuple = (1)
print(type(my_tuple))
my_tuple = (1.2)
print(type(my_tuple))
# to create a tuple 
# you need to 
my_tuple_2 = ("Max",)
print(type(my_tuple_2))
# just adding a commma ,

# accssing elements 
# very simular to list 
# cannot change elements 
my_tuple_2 = ("max", 1, 3, 6, 7, 8)
item = my_tuple_2[-1]  
print(item)

# iterating through tuple
for x in my_tuple_2:
	print(x)

# check if something in tuple 
if  "max" in my_tuple_2:
     print("yes")

else: 
	 print("no")

# get the length of tuple and looping over
for x in range(len(my_tuple_2)):
	print(my_tuple_2[x])


# find the frequence of a an element 

print(my_tuple_2.count("max")) # returns 1 we
# because we only have one max

# get the index of tuple

print(my_tuple_2.index("max"))
# return the index of the first occorance of max

# convert a tuple to a list
my_list = list(my_tuple_2)

print(my_list)
print(type(my_list))

# add a element to the new list 
my_list.append("mark")
print(my_list)

# covert list to tuple
my_tuple_2 = tuple(my_list)
print(my_tuple_2)

# slicing tuple 
# tutple slicing is the same as list
a = (1,2,3,4,5,6,7,8,9,10)
b = a[0:4]
print(b)

b = a[::2] # step arg 
print(b)

b = a[::-1] # reversing a tuple
print(b)


# adding tuples together
c = (11,12,13,14,15,16,17,18,19,20)
print(a+c)

# trick -- creating a tutple with 
# the same element 5 time or n times
d = (10,)*5

print(d)


# upacking a tutple 

person = ("sean", "peart", "25", "NJ")
first_name, last_name, age, location = person
# most match the amount of elements in the tuple
print(first_name)
print(last_name)
print(age)
print(location)

# unpacking to a list 

my_tutple_num = (1,2,3,4,5)

*one, two = my_tutple_num

print(one)

# will only unpack between 


# working with tuples can me more effiecent
# than working with list


