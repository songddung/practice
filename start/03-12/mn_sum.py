# swea 5188 최소합

T = int(input())


### DP
# def solve():
#     N = int(input())
#     ar = [list(map(int, input().split())) for _ in range(N)]
#     dp = [[0] * N for _ in range(N)]
#     dp[0][0] = ar[0][0]
#
#     for i in range(1, N):
#         dp[0][i] = dp[0][i - 1] + ar[0][i]
#         dp[i][0] = dp[i - 1][0] + ar[i][0]
#
#     for i in range(1, N):
#         for j in range(1, N):
#             dp[i][j] = ar[i][j] + min(dp[i - 1][j], dp[i][j - 1])
#
#     return dp[N - 1][N - 1]
#
#
# for t in range(1, T + 1):
#     print(f'#{t} {solve()}')


### teacher
def recur(y, x, mid):
    global result

    if mid > result:
        return

    if y == N - 1 and x == N - 1:
        result = min(result, mid)
        return

    # 아래로
    if y+1 < N:
        recur(y+1, x, mid+ar[y+1][x])

    if x+1 < N:
        recur(y, x+1, mid+ar[y][x+1])


for t in range(1, T + 1):
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(N)]

    result = N*N*10
    recur(0, 0, ar[0][0])
    print(f'#{t} {result}')
'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''
