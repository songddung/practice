# 토마토
# M, N = 열, 행
# 익음 :1, 안익음 : 0, 없으면 : -1
# 익은시간 반환
# BFS로 걸린시간 넣고
# 리스트를 탐색해서 가장 큰수를 구하고 -1해서 반환
# 리스트에 0 이 존재하면 -1 반환
from collections import deque

q = deque()
M, N = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]* M for _ in range(N)]
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(N):
    for j in range(M):
        if ar[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1
        if ar[i][j] == -1:
            visited[i][j] = -1

def bfs():
    while q:
        ci, cj = q.popleft()

        for k in range(4):
            dy, dx = ci + direct[k][0], cj + direct[k][1]
            if 0 <= dy < N and 0 <= dx < M and visited[dy][dx] == 0 and ar[dy][dx] != -1:
                q.append((dy, dx))
                visited[dy][dx] = visited[ci][cj] + 1
bfs()


def solve():
    mx = 0
    for i in range(N):

        if visited[i].count(0) > 0:
            return -1

        mx = max(max(visited[i]), mx)

    return mx - 1

print(solve())