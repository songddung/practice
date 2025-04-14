T = int(input())


def recur(k, mid):
    global result
    if k == N:
        result = min(result, mid+ar[path[-1]][0])
        return

    if mid > result:
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            path.append(i)
            recur(k+1, mid+ar[path[-2]][i])
            path.pop()
            used[i] = False


for t in range(1, T+1):
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(N)]

    result = 100 * N
    path = [0]
    used = [False] * N
    used[0] = True
    recur(1, 0)
    print(f'#{t} {result}')
