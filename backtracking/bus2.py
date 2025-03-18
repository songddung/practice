T = int(input())


def solve(cnt, battery, count):
    global result
    if count > result:
        return

    if cnt == N:
        result = min(result, count)
        return

    if battery:
        solve(cnt + 1, battery-1, count)
    solve(cnt + 1, ar[cnt]-1, count + 1)


for t in range(1, T + 1):
    N, *ar = map(int, input().split())
    ar = [0] + ar
    result = N
    solve(1, 0, -1)
    print(f'#{t} {result}')
