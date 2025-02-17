direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]


c,r = map(int,input().split())
k = int(input())

x = y = 0
ar = [[0] * c for _ in range(r)]

d = 0
s = 1

if k > r*c:
    print(0)

while s <= c*r: #
    if s == k:
        print(x+1, y+1)
    ar[y][x] = s

    dy = y + direct[d][0]
    dx = x + direct[d][1]

    if 0 <= dy < r and 0 <= dx < c and ar[dy][dx] == 0:
        y = dy
        x = dx
    else:
        d = (d + 1) % 4
        y, x = y + direct[d][0], x + direct[d][1]
    s += 1
