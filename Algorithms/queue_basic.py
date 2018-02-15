from collections import deque


print("demonstrate queue functionality\n")
queue_list=[1,2,3,4,5,6]
queue=deque(queue_list)
queue.append(7)
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
