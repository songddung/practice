def insert(v):
    idx = 1
    while tree[idx]:
        if tree[idx] < v:
            idx = idx * 2 + 1
        else:
            idx = idx * 2
    tree[idx] = v

N = 8
ar = [9, 4, 12, 3, 6, 15, 13, 17]
tree = [0] * 100

for data in ar:
    insert(data)
    print(tree)


def find(k):
    idx = 1
    while tree[idx]:  # 트리의 사이즈 제한 추가해야함
        if tree[idx] == k:
            return idx
        if tree[idx] < k:
            idx = idx * 2 + 1
        else:
            idx = idx * 2
    return -1

print(find(8))
print(find(17))
