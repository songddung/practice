T = int(input())

def solve():
    n = int(input())

    ar = [list(map(str, input())) for _ in range(n)]

    direct = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for i in range(n):
        for j in range(n):
            if ar[i][j] == 'o':
                for d in range(8):
                    count = 1
                    for h in range(1, 5):
                        dy = i + direct[d][0] * h
                        dx = j + direct[d][1] * h

                        if 0 <= dy < n and 0 <= dx < n and ar[dy][dx] == 'o':
                            count += 1
                        else:
                            break
                    if count == 5:
                        return 'YES'

    return 'NO'



for t in range(1, T+1):
    print(f'#{t} {solve()}')