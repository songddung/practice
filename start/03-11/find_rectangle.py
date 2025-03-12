from collections import deque
T = int(input())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(i, j, N, ar):
    q = deque()
    q.append((i, j))
    visited = [[0]*N for _ in range(N)]
    count = 0
    while q:
        ci, cj = q.popleft()

        for dy, dx in direct:
            ni, nj = ci + dy, cj + dx

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and ar[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                count += 1
    return count


def solve():
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(N):
            if ar[i][j] == 1:
                result = bfs(i, j, N, ar)
                if result == 0:
                    result = 1
                mx = max(mx, result)
    return mx


for t in range(1, T+1):
    print(f'#{t} {solve()}')