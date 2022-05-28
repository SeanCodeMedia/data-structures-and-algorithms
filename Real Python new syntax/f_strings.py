
first = "sean"
last  = "peart"

print(f" his first name is {first} and last name is {last}")
print(f" I want {first} to take me home")
print(f"hello {first} {last}")


## sorting 
mylist = ["cat", "rat", "bat", "sat", "mat", "hat", "tat", "fat"]
print("my sorted list in revsers is " + str(sorted(mylist, reverse=True)))
print("my sorted list is " + str(sorted(mylist)))

print("my sorted list is " + str(mylist.sort()))


# sets 

mySet = set()

mySet.add("a")
mySet.add("b")
mySet.add("c")
mySet.add("d")
mySet.add("h")

print(mySet)

#yield 

def getNumber():
    for r in range(1,10):
        yield r

g = getNumber()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# Break POINT 
#breakpoint()

#dictionaries 
# do math use full during lee code
d = {"a":5}

d["a"] += 8


print(d)