from collections import deque
def bfs(y, x):
    i = 2
    q = deque()
    q.append((y, x))

    while q:
        ci, cj = q.popleft()

        for dy, dx in direct:
            ni, nj = ci + dy, cj + dx

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = i
                i += 1

    return visited



N = int(input())
visited = [[0]*N for _ in range(N)]
y = x = 0
visited[y][x] = 1

direct = [(1, 0), (0, 1)]
result = bfs(y, x)

for i in result:
    print(*i)