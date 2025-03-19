T = int(input())


def make_set(x):
    return [i for i in range(x + 1)]


def find_set(x):
    if ar[x] == x:
        return x

    ar[x] = find_set(ar[x])
    return x


def union(x, y):
    idx = find_set(x)
    v = find_set(y)
    if idx == v:
        return
    ar[idx] = v


for t in range(1, T + 1):
    N, M = map(int, input().split())
    ar = make_set(N)
    uni = list(map(int, input().split()))

    for i in range(0, len(uni), 2):
        union(uni[i], uni[i + 1])

    for i in range(1, N + 1):
        find_set(i)

    print(f'#{t} {len(set(ar))-1}')

