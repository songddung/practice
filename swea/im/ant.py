c, r = map(int, input().split())
ar = [[0]*c for _ in range(r)]


x, y = map(int, input().split())
time = int(input())



direct = [(1, 1), (1, -1), (-1, -1), (1, -1)]
d = 0

for i in range(time):

    dy , dx = y+direct[d][0], x+direct[d][1]

    if dy < 0 or dy >= r+1 or dx < 0 or dx >= c+1:
        d += 1
        if d == 4:
            d = 0
    print(f'd : {d}')
    y += direct[d][0]
    x += direct[d][1]
    print(x, y)
print(x, y)


