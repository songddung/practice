

T = int(input())

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve():
    N = int(input())
    mx = 0
    mn = N*N*9 + 1
    ar = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            count = ar[i][j]
            for dy, dx in direct:
                for h in range(1,N):
                    ni , nj = i + dy*h, j + dx*h
                    if 0 <= ni < N and 0 <= nj < N:
                        count += ar[ni][nj]
            mx = max(mx, count)
            mn = min(mn, count)

    return mx-mn

for t in range(1, T+1):
    print(f'#{t} {solve()}')