# swea ladder1
# 100 * 100 배열
# 2에 도착하는 시작좌표의 x 출력
# 10개의 테스트케이스

T = 10
direct = [(0, 1), (0, -1)]
def solve():
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ar[i].count(2) == 1:
            y, x = i, ar[i].index(2)
            break

    while y >-1:
        for k in range(2):
            dy, dx = y + direct[k][0], x + direct[k][1]

            if 0 <= dy < 100 and 0 <= dx < 100:
                if ar[dy][dx] == 1:
                    ar[y][x] = 0
                    y = dy
                    x = dx

                    break
        else:
            y -= 1
    return N,x



for t in range(1, T+1):
    N, x= solve()
    print(f'#{N} {x}')
