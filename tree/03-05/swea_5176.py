T = int(input().strip())


def in_order(root, N, ar):
    global i
    if root <= N:
        in_order(root*2, N , ar)
        ar[root] = i
        i += 1
        in_order(root*2+1 , N ,ar)


def solve():

    N = int(input().strip())
    ar = [0] * (N+1)
    in_order(1, N, ar)
    return ar[1], ar[N//2]




for t in range(1, T+1):
    i = 1
    print(f'#{t}', *solve())