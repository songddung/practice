# 1번이 1개를 q에 넣음
# no, cnt 를 q에서 dequeue
# 출력
# 1번이 2개 넣음
# 2번이 1개 넣음
# no, cnt 를 q에서 dequeue
# 출력
q = []
new_num = 1
t = 0
while t < 20:
    q.append((new_num,1))
    new_num += 1
    no, cnt = q.pop(0)
    t += cnt
    # print(no, cnt, t)
    q.append((no, cnt+1))
    # print(q)
print(no)

### 덱
from collections import deque

q = deque()
new_num = 1
t = 0
while t < 20:
    q.append((new_num, 1))
    new_num += 1
    no, cnt = q.popleft()
    t += cnt
    q.append((no, cnt+1))

print(no)