# swea 5177 이진 힙

T = int(input())


def enq(node, ar, tree):
    global last_position
    last_position += 1
    tree[last_position] = node

    if last_position >= 2:
        c = last_position
        p = last_position // 2
        while c > 1 and tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            c = p
            p = p//2


def solve():
    N = int(input())
    ar = list(map(int, input().split()))

    tree = [0] * (max(ar) + 2)
    for i in ar:
        enq(i, ar, tree)

    idx = 0
    for i in range(len(tree)-1, 0, -1):
        if tree[i] != 0:
            idx = i
            break


    idx //= 2
    result = 0
    while idx >= 1:
        result += tree[idx]
        idx //= 2


    return result
for t in range(1, T+1):
    last_position = 0
    print(f'#{t} {solve()}')