T = int(input())
direct = ((1, 1), (1, -1), (-1, -1), (-1, 1))


def solve(y, x, cnt, start, dire):
    global result

    if dire > 3:
        return

    ni, nj = y + direct[dire][0], x + direct[dire][1]
    if (ni, nj) == start:
        result = max(cnt, result)
        return

    if dire < 3:
        ni2, nj2 = y + direct[dire + 1][0], x + direct[dire + 1][1]
        if (ni2, nj2) == start:

            result = max(cnt, result)
            return

        if 0 <= ni2 < N and 0 <= nj2 < N and ar[ni2][nj2] not in visited:
            visited.append(ar[ni2][nj2])
            solve(ni2, nj2, cnt + 1, start, dire + 1)
            visited.pop()

    if 0 <= ni < N and 0 <= nj < N and ar[ni][nj] not in visited:
        visited.append(ar[ni][nj])
        solve(ni, nj, cnt + 1, start, dire)
        visited.pop()


for t in range(1, T + 1):
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            visited = [ar[i][j]]
            count = 0
            solve(i, j, count, (i, j), 0)
    result = -1 if result == 0 else result + 1
    print(f'#{t} {result}')
