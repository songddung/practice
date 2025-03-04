# 길찾기

T = 10


def solve():
    tc, l = map(int, input().split())
    ar = list(map(int, input().split()))
    arr = [[] for _ in range(100)]
    visited = [0 for _ in range(100)]
    end = 99

    for i in range(0, l*2, 2):
        arr[ar[i]].append(ar[i+1])

    stack = [0]
    visited[0] = 1
    while stack:
        n = stack.pop(0)
        if n == end:
            return tc, 1
        for i in range(len(arr[n])):
            if arr[n][i] not in visited:
                stack.append(arr[n][i])
                visited[arr[n][i]] = 1

    return tc, 0






for t in range(1, T+1):
    tc, v = solve()
    print(f'#{tc} {v}')