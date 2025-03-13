T = int(input())


def solve(cnt, start):
    global mn
    if cnt == M:
        # print(path)
        ingre = list((set(range(0, N)) - set(path)))
        team1 = 0
        team2 = 0

        for i in range(len(path)):
            for j in range(i+1, len(path)):
                team1 += ar[path[i]][path[j]] + ar[path[j]][path[i]]

        for i in range(len(ingre)):
            for j in range(i+1, len(ingre)):
                team2 += ar[ingre[i]][ingre[j]] + ar[ingre[j]][ingre[i]]

        mn = min(mn, abs(team1 - team2))
        return

    for i in range(start, N-M+1+cnt):  # 4-2+1+cnt ==1+cnt
        path.append(i)
        # print(path)
        solve(cnt + 1, i + 1)
        path.pop()
        # print(path)


for t in range(1, T + 1):
    mn = 20000 * 8 + 1
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(N)]
    M = N // 2
    path = []
    solve(0, 0)

    print(f'#{t} {mn}')

'''
10
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
'''
