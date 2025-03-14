# 선반이어붙이기
# DFS
# 재귀
import time

T = int(input())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve(y, x, cnt):
    if len(cnt) == 7:
        result.add(cnt)
        return

    for dy, dx in direct:
        ni, nj = y+dy, x+dx
        if 0 <= ni < 4 and 0 <= nj < 4:
            solve(ni, nj, cnt+ar[ni][nj])


for t in range(1, T+1):
    ar = [list(input().split()) for _ in range(4)]
    result = set()
    start = time.time()
    for i in range(4):
        for j in range(4):
            solve(i, j, ar[i][j])
    end = time.time()
    print(end - start)
    print(f'#{t} {len(result)}')