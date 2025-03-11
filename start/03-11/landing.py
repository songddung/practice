T = int(input())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def solve():
    N, M = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            num = ar[i][j]
            count = 0
            for dy, dx in direct:
                ni, nj = i+dy, j+dx
                if 0 <= ni < N and 0 <= nj < M:
                    if ar[ni][nj] < num:
                        count += 1
                    if count >= 4:
                        result += 1
                        break
    return result


for t in range(1, T+1):
    print(f'#{t} {solve()}')