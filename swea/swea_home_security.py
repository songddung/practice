# 홈 방범 서비스
# N = 배열의 길이 (정사각형)
# M = 가구당 지불 최대 비용
# 손해보지 않고, 서비스 가능한 최대 가구수 리턴
# 운영비용 = bfs(k)의 칸수
# 수익 = 가구수 * M
# 이익 수익 - 운영비용
from collections import deque
T = int(input())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(which, N, ar):
    q = deque() # 큐 생성
    q.append(which) # 현재 위치 큐 삽입
    y, x = which
    visited = [[0] * N for _ in range(N)]

    visited[y][x] = 1
    if ar[y][x] == 1:
        arr = [0, 1]
    else:
        arr = [0]
    while q:
        ci, cj = q.popleft()
        for dy, dx in direct:
            ni, nj = ci + dy, cj + dx

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1

                if ar[ni][nj] == 1:
                    arr.append(visited[ni][nj])

    return arr


def solve():
    N, M = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(N)]
    mx = 0

    for i in range(N):
        for j in range(N):
            which = (i, j)
            arr = bfs(which, N, ar)

            arrr = [0] * (max(arr) + 1)

            for k in arr:
                if k != 0:
                    arrr[k] += 1

            for k in range(1, len(arrr)):
                arrr[k] += arrr[k - 1]
            # print(i, j, arrr)
            # print()
            for l in range(len(arrr)):
                if arrr[l]:
                    cost = l ** 2 + ((l - 1) ** 2)
                    revenue = M * arrr[l]
                    if cost <= revenue:
                        mx = max(mx, arrr[l])
            # print(i, j, mx)

    return mx


for t in range(1, T + 1):
    print(f'#{t} {solve()}')



