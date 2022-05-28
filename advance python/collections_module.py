# the collection module has container data structures 

from collections import Counter
from collections import namedtuple
from collections import OrderedDict 
from collections import defaultdict 
from collections import deque

a = "aaaaaaaaaaaabbbcccc"

# returns a dictionary 
my_counter = Counter(a)
# so now we can do dictionary operations
print(my_counter.items()) # return a list of tuples
print(my_counter.keys())
print(my_counter.values())

# most common items 
print(my_counter.most_common(1))  # first most common element
# returns a tuple  then we can access the values
print(my_counter.most_common(1)[0]) 
print(my_counter.most_common(1)[0][0]) 
print(my_counter.most_common(1)[0][1]) 

# convert a counter to a list 
print(list(my_counter.elements()))

# name tupled 
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x)
print(pt.y) 

# order_dict remembers the order an item was inserted
# into the dictionary.
#however, new python version built in dictionary remembers the order
# items are inserted 

ordered_dict = OrderedDict()
ordered_dict["a"] = "1"
ordered_dict["b"] = "2"
ordered_dict["c"] = "3"
ordered_dict["d"] = "4"
print(ordered_dict)

my_dict = {}
my_dict["a"] = 1
my_dict["b"] = 2
my_dict["c"] = 3
my_dict["d"] = 4
print(my_dict)

# notice the same result both dictionary and orderd dict kept the order

# will have a defualt key if we try to access a key that does not exitst
d = defaultdict(int) # you use any data type 
d['a'] = 1
d['b'] = 2
print(d.items())
print(d['a'])
print(d['b'])
print(d['c']) # notice 0 and we get now errors

#==================deque============================
# a deque is a double ended queue and we can remove and add elements from both ends in contstant time
my_deque = deque()
my_deque.append(1)
my_deque.append(2)
print(my_deque)
my_deque.appendleft(3)
print(my_deque)
my_deque.pop()
print(my_deque)
my_deque.popleft()
print(my_deque)

#----clear 
my_deque.clear()
print(my_deque)

#----extend
my_deque.extend([1,2,3,4])
print(my_deque)
# or 
my_deque.extendleft([5,6,7,8,9])

# rotation 
my_deque.rotate(2) # move all elements by 2 
print(my_deque)


# zip 

a = [1,3,5,7,9]
b = [2,4,6,8,10]


my_zip = zip(a, b)
for x in my_zip:
	print(f"{x[0]}, {x[1]}")