

# dictionary is unorderd data type that is mutable or dynamic
# we key value pair 

# creating and accessing values of dict
mydict = {"first":"sean", "last":"peart"}
print(mydict)


my_dic_two = dict(name="Marry", age=28, city="Newark")
print(my_dic_two)

print(mydict["first"])


# adding values to dict
mydict["email"] = "peart@msu.com"
print(mydict)


#---------------delete values 
# del mydict["first"]
# print(mydict)

# # POP  
# my_dic_two.pop("name")
# print(my_dic_two)

# # remove last item
# mydict.popitem()

# print(mydict)


# check if key in dict 

if "last" in mydict:
	print("yes")
else: 
	print("no")

# ------------looping

# for x in mydict:
# 	print(x)

# # or 

# # get the keys
# for x in mydict.keys():
# 	print(x)

# # get the values
# for x in mydict.values():
# 	print(x)

# # get the values 

# for x in mydict:
# 	mydict[x]
# ----get a list of keys 

my_keys = mydict.keys()
print(my_keys)

# --- get a list of values 
val = mydict.values()
print(val)

# items 
val = mydict.items()
print(val)

# copying dic

dic_1 = {"cat":"cat", "rat":"rat", "bat":"bat", "mat":"mat"}

# dic_2 = dic_1 


# dic_2["sat"] = "sat"

# print(dic_1)
# print(dic_2)

# oh no we modifiy both the dic_1 and dic_2 
# thats because we pointing to the same place
# in memory 

# now ---- the correct way of copying 

# dic_2 = dic_1.copy()
# dic_2["sat"] = "sat"

# print(dic_1)
# print(dic_2)

# or 
dic_2 = dict(dic_1)
dic_2["sat"] = "sat"

print(dic_1)
print(dic_2)
#--------------------merging-------------------------

dic_1.update(dic_2)
print(dic_1)


# keys ----------------------------------------------

# use a int as a key 

# tuple can be key 

# list cannot be a key a list is mutable and be changed
