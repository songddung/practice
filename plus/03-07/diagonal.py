from collections import deque
def bfs(y, x):
    result = []
    q = deque()
    q.append((y, x))
    visited = [[0]*M for _ in range(N)]
    visited[y][x] = 1
    result.append(ar[y][x])

    while q:
        ci, cj = q.popleft()

        for dy, dx in direct:
            ni, nj = ci + dy, cj + dx
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                result.append(ar[ni][nj])

    return result

N, M = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]
direct = [(0, 1),(1, 0)]
y = x = 0
result = bfs(y, x)
print(*result)
'''
3 4
1 2 3 4
5 6 7 8
9 10 11 12
'''