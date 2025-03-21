# # 최소 비용
#
#
# # dijkstra
# import heapq
#
#
# def solve():
#     dist = [[float('inf')] * N for _ in range(N)]
#     dist[0][0] = 0
#     pq = [(0, 0, 0)]
#
#     while pq:
#         cost, y, x = heapq.heappop(pq)
#
#         if cost > dist[y][x]:
#             continue
#
#         for dy, dx in direct:
#             ni, nj = y + dy, x + dx
#
#             if 0 <= ni < N and 0 <= nj < N:
#                 new_cost = max(0, ar[ni][nj] - ar[y][x])
#                 d = cost + new_cost + 1
#
#                 if d < dist[ni][nj]:
#                     dist[ni][nj] = d
#                     heapq.heappush(pq, (d, ni, nj))
#     return dist[-1][-1]
#
#
# T = int(input())
# direct = ((0, 1), (1, 0), (0, -1), (-1, 0))
# for t in range(1, T+1):
#     N = int(input())
#     ar = [list(map(int, input().split())) for _ in range(N)]
#     print(f'#{t} {solve()}')
#

from collections import deque


def solve(row, col):
    Q = deque()
    Q.append((row, col))
    visited[row][col] = 0
    while Q:
        row, col = Q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newR = row+dr
            newC = col+dc
            if 0 <= newR < N and 0 <= newC < N:
                diff = max(arr[newR][newC]-arr[row][col], 0)+1
                if visited[newR][newC] > visited[row][col] + diff:
                    visited[newR][newC] = visited[row][col] + diff
                    Q.append((newR, newC))

    # print(visited)
    return visited[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1e10]*N for _ in range(N)]

    print(f'#{tc} {solve(0, 0)}')
