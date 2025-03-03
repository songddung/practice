# 미로탐색
# BFS 최단거리
# 0,0에서 (N,M)까지 이동하는 최단거리
# N, M : 행, 열
# output : 최단거리


N, M = map(int, input().split())
ar = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
q = []
i = j = 0
q.append((i,j))
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited[i][j] = 1
def bfs():
    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (N-1, M-1):
            return visited[ci][cj]
        for k in range(4):
            dy, dx = ci + direct[k][0], cj + direct[k][1]
            if 0 <= dy < N and 0 <= dx < M and visited[dy][dx] == 0 and ar[dy][dx] == 1:
                q.append((dy, dx))
                visited[dy][dx] = visited[ci][cj] + 1


print(bfs())


