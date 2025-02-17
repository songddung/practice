# # ar = [3,6,7,1,5,4]
# # n = len(ar)
# #
# # for i in range(1 << n):
# #     for j in range(n):
# #         if i & (1 << j):
# #             print(ar[j], end=' ')
# #
# #     print()
#
# T = int(input())
#
# def solve():
#     direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     n = int(input())
#     ar = [list(map(int, input().split())) for _ in range(n)]
#     mx = 0
#     mn = 20*20*9+1
#
#
#     for i in range(n):
#         for j in range(n):
#             t = ar[i][j]
#             for step in direct:
#                 for h in range(1,n):
#                     dy, dx = i+step[0] *h, j + step[1]*h
#                     if 0 <= dy < n and 0 <= dx < n:
#                         t += ar[dy][dx]
#             if t > mx:
#                 mx = t
#             if t < mn:
#                 mn = t
#     return mx-mn
#
# for t in range(1, T+1):
#     print(f'#{t} {solve()}')

for i in range(1, 4):
      for j in range(1, 4):
          if j != i:
              for k in range(1, 4):
                  if k != i and k != j:
                      print(i, j, k)