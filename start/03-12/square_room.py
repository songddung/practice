T = int(input())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve(y, x, count, start):
    global mx, which
    for dy, dx in direct:

        ni, nj = y+dy, x+dx

        if 0 <= ni < N and 0 <= nj < N and ar[y][x] == ar[ni][nj] - 1:
            count += 1
            solve(ni, nj, count, start)

        if count > mx:
            mx = count
            which = start
        if count == mx:
            if which > start:
                which = start


for t in range(1, T+1):
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    which = 0
    for i in range(N):
        for j in range(N):

            start = ar[i][j]
            solve(i, j, 1, start)

    print(f'#{t} {which} {mx}')