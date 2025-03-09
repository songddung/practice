T = 10
N = 100

def is_pal(lst, leng):
    for arr in lst:
        for i in range(N-leng+1):
            if arr[i:i+leng] == arr[i:i+leng][::-1]:
                return True


def solve():

    tc = int(input())
    ar = [list(map(str, input())) for _ in range(N)]
    ar2 = list(map(list, zip(*ar)))

    for leng in range(N, 0, -1):
        if is_pal(ar, leng) or is_pal(ar2, leng):
            return tc, leng


for t in range(1, T+1):
    tc, v = solve()
    print(f'#{tc} {v}')