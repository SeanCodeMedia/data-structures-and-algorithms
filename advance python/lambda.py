
# syntax 
# lambda arguments:expression
from functools import reduce 

add10 = lambda x: x + 10 
print(add10(5))

# short hand way to write a function in oneline
subtract_one = lambda num: num-1
print(subtract_one(10))

mult = lambda x,y: x*y 
print(mult(10,2))
# you can give a defualt argument
mult = lambda x=2,y=30: x*y 
print(mult())

divide = lambda x,y: x//y 
print(divide(10,2))

# sorted method 

point2D = [(1,2), (15,1), (5, -1), (10,4)]
sorted_2D = sorted(point2D, key=lambda y: y[1])
print(point2D)
print(sorted_2D)


# map function 
#(func, seq)
a = [1,2,3,4,5]
b = map(lambda x: x * 2, a)
print(list(b))

# you can use list comprehension 
c = [x*2 for x in a]
print(c)


# filter function 

# filter(func, seq)
d = filter(lambda x:x%2 == 0, a)
print(list(d))

e = [x for  x in a if x%2 == 0] 
print(e)


# reduce(func, seq)
prod_a = reduce(lambda x,y:x*y, a)
print(prod_a)