T = int(input())

def solve():
    N = int(input())
    ar = []

    for i in range(1, N+1):
        arr = [1]*i
        if i >= 3:
            for k in range(1, len(arr)-1):
                arr[k] = ar[i-2][k] + ar[i-2][k-1]
        ar.append(arr)
    return ar

for t in range(1, T+1):
    print(f'#{t}')
    ar = solve()
    for i in ar:
        print(*i, sep=' ')