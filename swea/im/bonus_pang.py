T = int(input())

def solve():
    n = int(input())
    ar = [list(map(int, input().split())) for _ in range(n)]

    step = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    max_num = 0
    min_num = 20*20*9+1

    for i in range(n): # 행
        for j in range(n): # 열
            t = ar[i][j] # 초기 total : 자기 위치값
            for h in range(1, n): # 갈수있는칸
                for k in step:
                    dy = i + k[0] * h
                    dx = j + k[1] * h

                    if 0 <= dy < n and 0<= dx < n:
                        t += ar[dy][dx]

            if max_num < t:
                max_num = t
            if min_num > t:
                min_num = t
    return max_num - min_num
for t in range(1, T+1):
    print(f'#{t} {solve()}')