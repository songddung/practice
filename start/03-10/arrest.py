# 탈주범 검거
# 시간당 거리 1
# 7 종류 구조물
from collections import deque


def bfs(R, C, N, M, L, ar):
    q = deque()
    q.append((R, C))
    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1
    count = 1
    # print(L)

    while q:
        ci, cj = q.popleft()
        num = ar[ci][cj]
        num = str(num)
        # print(num)
        for dy, dx in direct[num]:
            # print(dy, dx)
            ni, nj = ci + dy, cj + dx
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and ar[ni][nj] != 0:
                if dy == 0 and dx == 1 and ar[ni][nj] in (3, 6, 7, 1):
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1
                    if visited[ni][nj] <= L:
                        count += 1

                if dy == 1 and dx == 0 and ar[ni][nj] in (2, 4, 7, 1):
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1
                    if visited[ni][nj] <= L:
                        count += 1

                if dy == 0 and dx == -1 and ar[ni][nj] in (3, 4, 5, 1):
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1
                    if visited[ni][nj] <= L:
                        count += 1

                if dy == -1 and dx == 0 and ar[ni][nj] in (2, 5, 6, 1):
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1
                    if visited[ni][nj] <= L:
                        count += 1
    # for i in visited:
    #     print(i)
    return count


def solve():
    N, M, R, C, L = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(N)]

    result = bfs(R, C, N, M, L, ar)
    return result


T = int(input())

direct = {
    '1': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    '2': [(1, 0), (-1, 0)],
    '3': [(0, 1), (0, -1)],
    '4': [(-1,0), (0, 1)],
    '5': [(1, 0), (0, 1)],
    '6': [(1, 0), (0, -1)],
    '7': [(-1, 0), (0, -1)]
}

for t in range(1, T+1):
    print(f'#{t} {solve()}')
