T = int(input())


def make_set(x):
    return [i for i in range(x + 1)]


def find_set(x):
    if ar[x] == x:
        return x

    ar[x] = find_set(ar[x])
    return ar[x]


for t in range(1, T+1):
    N, M = map(int, input().split())
    ar = make_set(N)
    for _ in range(M):
        idx, v = map(int, input().split())
        a, b = find_set(idx), find_set(v)
        if a == b:
            continue
        ar[a] = b

    my_set = set()
    for i in range(1, N+1):
        rep_i = find_set(i)
        my_set.add(rep_i)

    print(f'#{t} {len(my_set)}')

'''
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''