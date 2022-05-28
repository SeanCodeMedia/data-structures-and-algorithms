# a set is a collection data type 
# that us unorded and mutable but does not allow duplicates 


# creating a set 

my_set = {1,2,3,4,5}
print(my_set)

my_set = {1,2,3,4,5, 5}
print(my_set) # will only return on copy of the 5


my_set_1 = set("hello")
print(my_set_1) # order does not matter, notice one l

# if you want to have an empty set you have to use set() method
# for example 

# my_set_2 = {}

# print(type(my_set_2)) # will return the dict type 

# # not what we want so to create a set you need to do 

my_set_2 = set({})

print(type(my_set_2))  # now we have a set :) 


# mutining the set -- its mutable 
# --------------------------------- adding set
my_set_2.add(1)
my_set_2.add(2)
my_set_2.add(3)
my_set_2.add(4)
my_set_2.add(5)
my_set_2.add(6)

print(my_set_2)

# --------------------------------removing from set 
my_set_2.remove(1)
print(my_set_2)
# or 
my_set_2.discard(2) # but if it does not find the 
# element will not give an error exception
print(my_set_2)

# ---------------clearing the set
# my_set_2.clear()
# print(my_set_2) # empty set


# ---------pop--------------
my_set_2.pop() # remove the first element


#------------for loop------------

for i in my_set_2:
	print(i)

# ----------------------------
# not set does not have index 

if 6 in my_set_2:
	print("yes")

else:
	print("no")

if 9 in my_set_2:
	print("yes")

else:
	print("no")


# -------Union and intersection-------


odd = set({1, 3, 5, 7, 9})
even = set({0, 2, 4, 6, 8, 10})
prime  = set({2, 3, 5, 7})

u = odd.union(even)

print(u)

# intersection 
i = odd.intersection(even)
print(i)

i = odd.intersection(prime)
print(i)

# ----------------difference-------------

setA = set({1,2,3,4,5,6,7,8,9})
setB = set({1,2,4,5,10,11,12})

diff = setA.difference(setB)  # can call update to change in palce
print(diff) # will return a new set 


# symmetric_difference

diff_2 = setA = setA.symmetric_difference(setB)
print(diff_2) # will return a new set not in place 


#-------------------update----------------
# will also merge set  
setA.update(setB) # modify in place 

print(setA)


# --------------is subset-------------------------

setC = ({1,2,3,4,5,6,7,8,9})
setD = ({1,2,3})
print(setC.issubset(setD))
print(setD.issubset(setC))


#_------------------ super set 
print(setC.issuperset(setD))
print(setD.issuperset(setC))

#---------------copy sets-----------------------

# wrong --- :)
# setE = ({1,2,3,5,6})
# setG = setE 
# setG.add(10)
# print(setE)
# print(setG)

# wrong 

# setE = ({1,2,3,5,6})
# setG = setE.copy()
# setG.add(10)
# print(setE)
# print(setG)

# or

setE = ({1,2,3,5,6})
setG = set(setE)
setG.add(10)
print(setE)
print(setG)

# frozenset 

# a frozen set cannot be changed after creation 

a = frozenset([1,2,3,5])
# union and intersection will work but add and remove
# will not work
print(a)