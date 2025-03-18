# 장훈이의 높은 선반
# 조합 구해서 각 조합의 합이 M이하 중 최대 = mx
# M - mx 리턴

T = int(input())


def solve(cnt, start):
    global mn

    print(path)
    if cnt > len(ar):  #
        return

    if mn > sum(path) >= M:
        mn = sum(path)

    for i in range(start, len(ar)):
        path.append(ar[i])
        solve(cnt + 1, i+1)
        path.pop()


for t in range(1, T+1):
    N, M = map(int, input().split())
    ar = list(map(int, input().split()))
    mn = sum(ar)
    path = []
    solve(0, 0)
    print(f'#{t} {mn-M}')
