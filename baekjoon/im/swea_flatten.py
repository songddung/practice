T = 10


def solve():
    i = int(input())
    ar = list(map(int, input().split()))



    while i >= 0:
        top = max(ar)
        bottom = min(ar)
        if top - bottom <= 1:
            return top - bottom
        mx_idx = ar.index(top)
        mn_idx = ar.index(bottom)
        ar[mx_idx] -= 1
        ar[mn_idx] += 1
        i -= 1


    return top - bottom

for t in range(1, T+1):
    print(f'#{t} {solve()}')