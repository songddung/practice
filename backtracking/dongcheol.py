T = int(input())


def solve(cnt, total):
    global result

    if cnt == N:
        result = max(result, total)
        return

    for i in range(len(ar[0])):
        if not visited[i]:
            if total * (ar[cnt][i] / 100) <= result:
                continue
            visited[i] = 1
            solve(cnt + 1, total * (ar[cnt][i] / 100))
            visited[i] = 0


for t in range(1, T + 1):
    N = int(input())
    visited = [0] * N
    result = 0

    ar = [list(map(int, input().split())) for _ in range(N)]
    solve(0, 1)

    print(f'#{t} {result * 100:.6f}')