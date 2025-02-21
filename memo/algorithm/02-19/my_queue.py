### 선형큐

n = 3
front = rear = -1
Q = [0] * n


# 삽입
def en_queue(item):
    global rear
    if is_full():
        print('Queue_full')
    else:
        rear += 1
        Q[rear] = item


# 삭제
def de_queue():
    global front
    if is_empty():
        print('Queue_empty')
    else:
        front += 1
        return Q[front]


# 포화 확인
def is_full():
    return rear == len(Q) - 1


# 공백 상태 확인
def is_empty():
    return front == rear


def q_peek():
    if is_empty():
        print('Queue_empty')
    else:
        return Q[front + 1]


en_queue(1)
en_queue(2)
en_queue(3)
print(Q)


while front != rear:
    t = de_queue()
    print(t)

### 원형큐
queue = []
def en_queue(item):
    global rear
    if is_full():
        print('queue_full')
    else:
        rear += 1 % n
        queue[rear] = item

def de_queue():
    global front
    if is_empty():
        print('queue_empty')
    else:
        front += 1 % n
        return queue[front]

def is_full():
    global front
    global rear
    return (rear+1) % len(queue) == front


def is_empty():
    global front
    global rear
    return front == rear

