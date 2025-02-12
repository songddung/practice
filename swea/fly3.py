T = int(input())

p_step = [[(-1,0), (0,1), (1,0), (0,-1)] , [(-1,-1), (-1,1), (1,1), (1,-1)]]


def solve():
    n, m = map(int, input().split())
    max_num = 0
    ar = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n): # 행
        for j in range(n): # 열

            for k in range(2): #  + , X 스탬
                which = ar[i][j]
                for h in range(4): # 상하좌우
                    for g in range(1,m): # 스프레이 세기
                        dx, dy = i + p_step[k][h][0] * g, j + p_step[k][h][1] * g

                        if 0 <= dx < n and 0 <= dy < n:
                            which += ar[dx][dy]
                if max_num < which:
                    max_num = which

    return max_num
for t in range(1,T+1):
    print(f'#{t} {solve()}')