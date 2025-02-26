N = int(input())
ar = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):
    col, row, width, height = map(int, input().split())

    for r in range(row, row+height):
        ar[r][col:col+width] = [n] * width


for n in range(1, N+1):
    total = 0
    for i in range(1001):
        total += ar[i].count(n)
    print(total)