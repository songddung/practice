# T = int(input())
#
# step = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#
# def solve():
#     n = int(input())
#     ar = [list(map(int, input().split())) for _ in range(n)]
#
#     max_num = 0
#     min_num = 100*10000
#     for i in range(n): # 행
#         for j in range(n): # 열
#             which = ar[i][j] # 현재위치
#             for k in range(4): # 상하좌우
#                 for l in range(1, n): # 끝까지
#                     dy, dx = i + (step[k][0] * l), j + (step[k][1] * l)
#
#                     if 0 <= dy < n and 0 <= dx < n:
#                         which += ar[dy][dx]
#             if min_num > which:
#                 min_num = which
#             if max_num < which:
#                 max_num = which
#     return max_num - min_num
# for t in range(1,T+1):
#     print(f'#{t} {solve()}')


T = int(input())

def solve():
    n = int(input())
    ar = [list(map(int, input().split())) for _ in range(n)]
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    mx = 0
    mn = n * n * 9 + 1


    for i in range(n): # 행
        for j in range(n): # 열
            t = ar[i][j] # 현재위치
            for d in range(4): # 4방향
                for h in range(1, n): # 끝까지
                    dy, dx = i + direct[d][0]*h , j + direct[d][1]*h
                    if 0 <= dy < n and 0 <= dx < n:
                        t += ar[dy][dx]
            if t < mn:
                mn = t
            if t > mx:
                mx = t
    return mx-mn
for t in range(1, T+1):
    print(f'#{t} {solve()}')


