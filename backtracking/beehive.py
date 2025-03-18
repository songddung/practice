T = int(input())


def ghs(lst):  # good_honey_select
    mx = 0
    path = []

    def backtrack(idx, subset):
        if idx == len(lst):
            path.append(subset[:])
            return

        subset.append(lst[idx])
        backtrack(idx+1, subset)
        subset.pop()
        backtrack(idx+1, subset)

    backtrack(0, [])

    for p in path:
        if sum(p) > C:
            continue
        mx = max(mx, p**p)


def solve(y, x):
    if x > N-M+1:
        y += 1
        x = 0
    if y == N:
        return

    hive2 = ar[y][x:x+M]

    if sum(hive2) > C:
        ghs(hive2)

    solve(y, x+M)




for t in range(1, T+1):
    result = 0
    N, M, C = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            hive1 = ar[i][j:j+M]


    print(f'#{t} {result}')
