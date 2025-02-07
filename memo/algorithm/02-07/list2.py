'''
3
1 2 3 0
4 5 6 0
7 8 9 0
'''

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
print(arr)

# ### 0으로 채워진 3*4 배열
# arr = [[0] * 4 for i in range(3)]
# print(arr)



### 행우선 순회
for i in range(N):
    for j in range(N):
        print(arr[i][j])

### 열 우선 순회
for j in range(N):
    for i in range(N):
        print(arr[i][j])

### 지그재그 순회
for i in range(N):
    for j in range(N+1):
        print(arr[i][j + (N-1-2*j) * (i%2)])

