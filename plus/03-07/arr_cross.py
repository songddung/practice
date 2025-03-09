from collections import deque
def bfs():
    y = x = 0
    q = deque()
    q.append((y, x))
    result = [[] for _ in range(N+M)]

    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    result[1] = [1]
    while q:
        ci, cj = q.popleft()

        for dy, dx in direct:
            ni, nj = ci + dy, cj + dx

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                num = visited[ni][nj]
                result[num].append(ar[ni][nj])

    return result





direct = [(0, 1), (1, 0)]
N, M = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]
result = bfs()
for i in result:
    if i:
        print(sum(i))


