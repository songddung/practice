T = 10

def in_order(root, N, ar):
    global result
    if root <= N:
        in_order(root*2,N,ar)
        result += ar[root]
        in_order(root*2+1, N, ar)

    return result



def solve():
    N = int(input())
    ar = [0] * (N+1)
    for _ in range(N):
        idx, v, *t = map(str, input().split())
        ar[int(idx)] = v

    print(ar)

    return in_order(1, N, ar)

for t in range(1, T+1):
    result = ''
    print(f'#{t} {solve()}')

'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''