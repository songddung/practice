T = int(input())

def solve():
    n = int(input())

    ar = [list(map(str, input())) for _ in range(n)]

    direct = [(1, 0), (0, 1), (0, -1)]

    for i in range(n):
        for j in range(n):
            if ar[i][j] == 'o':
                for st in direct:
                    count = 1
                    for h in range(1, n):
                        dy = i + st[0] * h
                        dx = h + st[1] * h

                        if 0 <= dy < n and 0 <= dx < n:
                            if ar[dy][dx] == 'o':
                                count += 1
                    if count == 5:
                        return 'YES'

    return 'NO'



for t in range(1, T+1):
    print(f'#{t} {solve()}')