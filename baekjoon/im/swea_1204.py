# 최빈수구하기

T = int(input())


def solve():
    tc = int(input())
    ar = list(map(int, input().split()))
    arr = [0] * 101
    for i in ar:
        arr[i] += 1

    mx = 0
    idx = 0
    for i in range(len(arr)):
        if mx <= arr[i]:
            mx = arr[i]
            idx = i

    return tc, idx

for t in range(1, T + 1):
    tc , v  = solve()
    print(f'#{tc} {v}')