# 자리배정

c, r = map(int, input().split())
check = int(input())
ar =[[0]*c for _ in range(r)]

direct = [(1, 0), (0 ,1), (-1, 0), (0, -1)]




def solve():
    y = x = 0
    d = 0

    i = 1

    if check > r*c:
        return 0

    while i < r*c+1:
        if i == check:
            return (x + 1, y + 1)
        ar[y][x] = i

        dy, dx = y + direct[d][0], x + direct[d][1]

        if 0 <= dy < r and 0 <= dx < c and ar[dy][dx] == 0:
            y, x = dy , dx

        else:
            d += 1
            if d == 4:
                d = 0
            y, x = y + direct[d][0], x + direct[d][1]
        i += 1
result = solve()
if type(result) == tuple:
    print(*result)
else:
    print(result)

