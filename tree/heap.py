# heap : 우선순위 큐를 사용할때 많이 사용
# 최대 힙 : 루트가 가장 큰 값 > 부모노드가 자식노드보다 값이 커야 함
# 최소 힙 : 루트가 가장 작은 값 > 부모노드가 자식노드보다 값이 작아야 함


def enq(v):
    global last_position

    last_position += 1
    tree[last_position] = v


    c = last_position
    p = last_position // 2
    while c > 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = p//2


def deq():
    global last_position
    result = tree[1]
    tree[1] = tree[last_position]
    last_position -= 1

    p = 1
    c = p*2  # left
    while c <= last_position:  # c는 left를 유지하도록
        if c+1 <= last_position and tree[c] < tree[c+1]:
            c = c+1

        if tree[p] < tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2
        else:
            break

    return result


tree = [0, 20, 15, 19, 4, 13, 11] + [0]*100
last_position = 6
print(tree)
enq(23)
print(tree)
# enq(21)
# print(tree)
# enq(1)
# print(tree)
print(deq())
print(tree)
print(tree[0:last_position+1])