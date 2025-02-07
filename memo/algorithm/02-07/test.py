### 대각선 합계
#
# N = 5
# s = 0
# for i in range(5):
#     s += A[i][i]
#     s += A[i][N-1-i]
#
#
# s -= A[N//2][N//2]


aij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
### 연습문제

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
total = 0
for i in range(N):
    for j in range(N):
        for di, dj in aij:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                total += abs(arr[ni][nj] - arr[i][j])
print(total)