import collections

my_queue =  collections.deque()

my_queue.append("hello")
my_queue.appendleft("Sun")
my_queue.appendleft("Sat")
my_queue.popleft()
my_queue.pop()
print(my_queue)