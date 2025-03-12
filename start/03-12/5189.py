# swea 5189 전자카트

T = int(input())


def recur(cnt, N, used, ar):
    global mn
    if cnt == (N - 1):
        # print(path)

        total = 0
        num = 0

        for i in path:
            total += ar[num][i]
            num = i
        total += ar[num][0]
        if total < mn:
            mn = total
        return

    for i in range(N - (N - 1), N):
        # print(i)
        if used[i] == 0:
            used[i] = 1
            path.append(i)
            recur(cnt + 1, N, used, ar)
            path.pop()
            used[i] = 0


def solve():
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * (N + 1)

    recur(0, N, used, ar)
    return mn


for t in range(1, T + 1):
    path = []
    mn = 10001

    print(f'#{t} {solve()}')
