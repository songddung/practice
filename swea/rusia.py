# T = int(input())
#
# def solve():
#     n, m = map(int, input().split())
#
#     ar = [list(map(str, input())) for _ in range(n)]
#     max_num = 0
#
#     for i in range(n - 2): # 화이트 범위 (처음부터 마지막 전전 줄 까지
#         for j in range(i + 1, n - 1): # 블루 범위 ( 화이트 다음줄부터 ~ 마지막 전 줄 까지
#             t = 0
#
#             for k in range(i + 1):
#                 t += ar[k].count('W')
#
#             for k in range(i + 1, j + 1):
#                 t += ar[k].count('B')
#
#             for k in range(j + 1, n):
#                 t += ar[k].count('R')
#
#             if max_num < t:
#                 max_num = t
#     return n*m-max_num
#
# for t in range(1, T+1):
#     print(f'#{t} {solve()}')


T = int(input())

def solve():
    n, m = map(int,input().split())
    ar = [list(map(str, input())) for _ in range(n)]
    mx = 0
    for i in range(0, n-2):  # 0 ~ 1
        for j in range(i+1, n-1):  # i+1 ~ 2
            total = 0

            for k in range(i+1):
                total += ar[k].count('W')

            for k in range(i+1, j+1):
                total += ar[k].count('B')

            for k in range(j+1,n):
                total += ar[k].count('R')

            if mx < total:
                mx = total

    return n*m-mx

for t in range(1, T+1):
    print(f'#{t} {solve()}')




