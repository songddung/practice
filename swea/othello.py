T = int(input())

def solve():
    n, m = map(int, input().split())
    ar = [[0]*n for _ in range(n)]
    arr = []
    for i in range(m):
        arr.append(list(map(int, input().split())))

    # 초기 세팅
    half = n//2-1
    ar[half][half] = 1
    ar[half][half+1] = 2
    ar[half+1][half] = 2
    ar[half+1][half + 1] = 1

    direct = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]

    for i in range(m):
        end = 0
        for e in ar:
            end += e.count(0)
        if end == 0:
            break

        x, y, c = arr[i]
        y -= 1
        x -= 1

        ar[y][x] = c

        for st in direct:  # 8 방향
            dy, dx = y + st[0], x + st[1]

            if 0 <= dy < n and 0 <= dx < n:
                if ar[dy][dx] == c or ar[dy][dx] == 0:  # 다음 칸이 같은 색이거나 빈 칸이면
                    continue  # 다음 방향으로 계속 진행

                i = 1  # 반대 색 돌의 개수
                while 0 <= dy < n and 0 <= dx < n:
                    py, px = dy, dx

                    if ar[py][px] == c:  # 같은 색을 찾으면
                        # 사이의 돌을 뒤집기
                        for k in range(1, i):
                            ar[y + st[0] * k][x + st[1] * k] = c
                        break

                    elif ar[py][px] == 0:  # 빈 칸을 찾으면
                        break

                    else:  # 현재칸이 다른 색 돌이면
                        dy += st[0]
                        dx += st[1]
                        i += 1

    black = sum(row.count(1) for row in ar)
    white = sum(row.count(2) for row in ar)

    return black, white



for t in range(1, T+1):
    print(f'#{t}', *solve())

