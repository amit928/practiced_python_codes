
# stack=list()
# stack.append('a')
# stack.append('b')
# stack.append('c')
# print(stack)
# stack.pop()
# print(stack)
# stack.pop(1)
# print(stack)

'''collections.dequeue'''

# import collections
# x=collections.deque([2,3,4,5])
# print(x)
# x.append(6)
# print(x)
# x.appendleft(1)
# print(x)
# x.pop()
# print(x)
# x.popleft()
# print(x)
# x.remove(3)
# print(x)

'''queue.LifoQueue'''

import queue
x=queue.LifoQueue(maxsize=5)
print(x.qsize())
x.put(1)
x.put(2)
x.put(3)
x.put(4)
print(x.full())
print(x.get())
print(x.get())
print(x.get())
print(x.get())
print(x.empty())
