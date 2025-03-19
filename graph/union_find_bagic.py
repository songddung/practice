# 서로소 집합
# 6개의 원소(1 ~ 6)
# 각 집합 생성
def make_set(n):
    p = [i for i in range(N+1)]
    return p


# def find_set(x):
#     if parents[x] == x:
#         return x
#     return find_set(parents[x])

# 경로 압축
def find_set(x):
    if parents[x] == x:
        return x
    # path compression => x의 부모를 대표자로
    # parents[x] = find_set(parents[x])

    # 모든 노드의 대표자를 변경
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):
    idx = find_set(x)
    v = find_set(y)
    if idx == v:
        return
    parents[idx] = v


N = 6
parents = make_set(N)
print(find_set(6))
union(3, 6)
print(parents)
