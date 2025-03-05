T = int(input())

def post_order(ar, n):
    pass



def solve():
    N, M, L = map(int, input().split())
    ar = [0]*(N+1)

    for _ in range(M):
        n, v = map(int, input().split())
        ar[n] = v

    post_order(ar, N)

for t in range(1, T+1):
    print(f'#{t} {solve()}')