### sw 문제 해결
#

N = int(input())
ar = [[0]*7 for _ in range(2)]
a = N

for i in range(0, 4):
    ar[0][i] = a
    a += 1

b = N
for j in range(6, 2, -1):
    ar[1][j] = b
    b -= 1
print(ar)

