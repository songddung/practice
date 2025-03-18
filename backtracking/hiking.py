T = int(input())
direct = ((0, 1), (1, 0), (0, -1), (-1, 0))


def solve(y, x, iscut, check):
    global result, mx_num

    visited[y][x] = 1
    mx_num += 1
    for dy, dx in direct:
        ni, nj = y + dy, x + dx

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if ar[ni][nj] < check:

                solve(ni, nj, iscut, ar[ni][nj])
            else:
                if iscut == 0 and ar[ni][nj]-K < check:
                    solve(ni, nj, 1, ar[ni][nj] - 1)

    visited[y][x] = 0
    result = max(mx_num, result)
    mx_num -= 1


for t in range(1, T + 1):
    N, K = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):  # 배열의 최대 값 찾기
        mx = max(max(ar[i]), mx)

    result = 0

    for i in range(N):
        for j in range(N):
            if ar[i][j] == mx:
                mx_num = 0
                visited = [[0] * N for _ in range(N)]
                solve(i, j, 0, ar[i][j])
    print(f'#{t} {result}')






