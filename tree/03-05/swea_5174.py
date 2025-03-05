# subtree

T = int(input())


def post_order(n, left, right):
    global cnt

    if n:
        post_order(left[n], left, right)
        post_order(right[n], left, right)
        cnt += 1



def solve():
    E, N = map(int, input().split())
    ar = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E + 2)
    # print(ar)

    for i in range(E):
        if left[ar[2*i]] == 0:
            left[ar[2*i]] = ar[2*i+1]
        else:
            right[ar[2*i]] = ar[2*i+1]
    # print(left)
    # print(right)
    post_order(N, left, right)

    return cnt



for t in range(1, T+1):
    cnt = 0
    print(f'#{t} {solve()}')

'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''