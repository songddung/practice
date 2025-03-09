# N,M : 행, 열

N, M = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]
ar2 = [list(map(int, input().split())) for _ in range(N)]
result = []
for i in range(N):
    arr = []
    for j in range(M):
        arr.append(ar[i][j] + ar2[i][j])
    result.append(arr)

for i in range(N):
    print(*result[i])
