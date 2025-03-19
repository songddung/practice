def solve(node, cnt):
    global mx
    visited[node] = 1
    mx = max(mx, cnt)
    for i in ar[node]:
        if not visited[i]:
            solve(i, cnt+1)
    visited[node] = 0


T = int(input())
for t in range(1, T+1):

    N, M = map(int, input().split())
    ar = [[] for _ in range(N+1)]
    for i in range(M):
        idx, v = map(int, input().split())
        ar[idx].append(v)
        ar[v].append(idx)
    mx = 1

    for i in range(1, N+1):
        visited = [0] * (N + 1)
        solve(i, 1)
    print(f'#{t} {mx}')

'''
1
3 2
1 2
3 2
'''