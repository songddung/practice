T = int(input())


def solve():
    N = int(input())
    ar = list(map(int, input().split()))
    mx = 0
    for i in range(N-1):
        lst = [0]
        for j in range(i+1, N):
            if ar[i] < ar[j]:
                if lst[-1] < ar[j]:
                    lst.append(ar[j])

        mx = max(len(lst)-1, mx)

    return mx


for t in range(1, T+1):
    print(f'#{t} {solve()}')