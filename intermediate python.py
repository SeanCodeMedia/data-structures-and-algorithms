

# list  

mylist = ["Apple", "Banana", "cherry"]

# accssing and looping over
#------------------------------
# print(mylist[-3])

# for x in mylist:
# 	print(x)

# if 9 in mylist:
# 	print("yes")
# else:
# 	print("no")

# remove last element if nothing is pass to it 
# remove base on index if the index is pass to the pop method
#--------------remove------------
item = mylist.pop() 
item = mylist.pop(0) 
print(item)
print(mylist)
mylist.remove("Banana")
print(mylist)
# ----------clear---------------

mylist_2 = [0 for x in range(1,11)] # list comprehension 
print(mylist_2)
mylist_2.clear()
print(mylist_2)

#-----------reverse--------------
mylist_3 = [x for x in range(1,11)]
print(mylist_3)
mylist_3.reverse()
print(mylist_3)

#----------sort--------------------
my_new_list = sorted(mylist_3) # create a new list
print(my_new_list)
print(mylist_3) # this is the orgingal list 
mylist_3.sort() # the list is sorted in place here
print(mylist_3)

#----------------trick--------------
'''
if you want a list with the same element you can just do 
this
'''
zeros_list = [0] * 10
print(zeros_list)

one_list = [1] * 10
# ------------ADDING LIST TOGETHER------------
print(zeros_list+one_list)

#------------slicing a list---------------------

mylist_4 = [x for x in range(10, 20)]

print(mylist_4)

mid_point = len(mylist_4)//2 
print(mylist_4[mid_point:])
print(mylist_4[:mid_point])

# or you can do this 
a = mylist_4[2:4]
print(a)

# steps -----------------------------------------

print(mylist_4[::2]) # prints every other element 
#in the list 

# trick---------------reverse---------------------

print(mylist_4[::-2]) # you can reverse every step


#----------------copy-----------------------------

fruits = ["banana", "apple", "cherry", "kiwi"]

# fruits_copy = fruits
# print(fruits_copy)
# fruits_copy.append("lemon")
# print(fruits_copy) # but this modifiy the orginal
# print(fruits) # did not know this but both list are the same location in memeory :()

# instead use .copy method
# now it works 
# fruits_copy = fruits.copy()
# print(fruits_copy)
# fruits_copy.append("lemon")
# print(fruits_copy)
# print(fruits) 

#----------------another way to copy----------------------------------
# fruits_copy = list(fruits)
# print(fruits_copy)
# fruits_copy.append("lemon")
# print(fruits_copy)
# print(fruits) 
#----------------another way to copy----------------------------------
fruits_copy = fruits[:]
print(fruits_copy)
fruits_copy.append("lemon")
print(fruits_copy)
print(fruits) 

# list comprehension ------------------------------------------------

# syntax = [expression for loop over your list]
new_list_1 = [x for x in range(1, 10)]
new_list_2 = [i*i for i in new_list_1]
print(new_list_2)
new_list_3 = [i+i for i in new_list_2]
print(new_list_3)