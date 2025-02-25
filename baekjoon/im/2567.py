ar = [[0]*101 for _ in range(101)]

n = int(input())

for _ in range(n):
    col, row = map(int, input().split())
    for i in range(row, row+10):
        for j in range(col, col+10):
            ar[i][j] = 1

boundary = 0
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(101):
    for j in range(101):
        if ar[i][j] == 0:
            for k in range(4):
                dy, dx = i + direct[k][0], j + direct[k][1]
                if 0 <= dy < 101 and 0 <= dx < 101:
                    if ar[dy][dx] == 1:
                        boundary += 1

print(boundary)

