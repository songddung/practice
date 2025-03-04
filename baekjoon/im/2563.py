# 색종이
ar = [[0] * 100 for _ in range(100)]

n = int(input())
arr = []
for i in range(n):
    arr.append(map(int, input().split()))

for i, j in arr:
    for row in range(j, j+10):
        for col in range(i, i+10):
            ar[row][col] = 1

num = 0
for i in range(100):
    num += sum(ar[i])

print(num)