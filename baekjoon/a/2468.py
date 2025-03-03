# # 안전 영역
# # N : 행, 열의 길이
# # 물의 높이를 하나씩 증가시켜 안전하지 않은 그룹이 가장 많을 때 반환



from collections import deque

N = int(input())
ar = [list(map(int, input().split())) for _ in range(N)]
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(start_i, start_j, h):
    q = deque()
    q.append((start_i, start_j))
    visited[start_i][start_j] = 1

    while q:
        ci, cj = q.popleft()
        for dy, dx in direct:
            ni, nj = ci + dy, cj + dx
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and ar[ni][nj] > h: # 범위 내, 방문x, 안전영역
                visited[ni][nj] = 1
                q.append((ni, nj))

mx = 0
for h in range(101):  # 물의 높이를 0부터 100까지 증가
    visited = [[0] * N for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if ar[i][j] > h and visited[i][j] == 0:  # 현재 높이보다 높은 지역
                bfs(i, j, h)  # BFS 호출
                result += 1  # 안전 영역 개수 증가

    mx = max(result, mx)  # 최대 안전 영역 개수 업데이트

print(mx)
