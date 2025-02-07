di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
n = 2
m = 3
### 1번째 방법
for i in range(n):
    for j in range(m):
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < n and 0 <= nj < m:
                print(ni, nj)

print('##############################################################')


aij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
### 2번째 방법
for i in range(n):
    for j in range(m):
        for di, dj in aij:
            ni = i+di
            nj = j+dj
            if 0 <= ni < n and 0 <= nj < m:
                print(ni, nj)


### 응용 상하좌우 k칸 합계 중 최대값(k=2)
max_v = 0
N = 8
M = 8
K = 2
for i in range(N):
    for j in range(M):
        s = arr[i][j]
        for di, dj in dij:
            for c in range(1, K+1):
                ni, nj = i+di*c, j+dj*c
                if 0 <= ni < N and 0<= nj < N:
                    s += arr[ni][nj]
        if max_v < s :
            max_v = s


### 전치 행렬
arr = [[1,2,3,],[4,5,6],[7,8,9]]

for i in range(len(arr)):
    for j in range(len(arr[0])):            # for j in range(i): 인 경우 
if i < j :                                  # if문 필요 없음
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]