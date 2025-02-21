from collections import deque

q = deque()
q.append(1)     # enqueue()
t = q.popleft() # dequeue()

list_q = []
for i in range(2**63):
    list_q.append(i)
for _ in range(2**63):
    list_q.pop(0)
print('end')
# deque_q = deque()
# for i in range(1000000):
#     deque_q.append(i)
# for _ in range(1000000):
#     deque_q.popleft()
# print('end')
