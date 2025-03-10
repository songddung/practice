T = int(input())


def solve():
    N = int(input())
    ar = list(map(int, input().split()))
    lst = []
    mx = max(ar)
    result = 0
    for i in range(len(ar)):
        if ar[i] < mx:
            result += mx - ar[i]
        if i < len(ar)-1 and ar[i] == mx:
            mx = max(ar[i+1:])
    return result


for t in range(1, T+1):
    print(f'#{t} {solve()}')