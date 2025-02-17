# ar = [1,2,3]
#
# ar[0] = 2 if ar[0] == 1 else  3
#
# print(ar)


### 백준 스위치
# n = int(input())
# ar = list(map(int, input().split()))
#
# m = int(input())
# arr = [map(int,input().split()) for _ in range(m)]
#
#
# for i in range(m):
#     gen, idx = arr[i]
#
#     if gen == 1:
#         which = idx - 1 # 현재위치
#         jump = n // idx # 점프 횟수
#
#         for j in range(jump):
#             if ar[which + j*idx ] == 0 :
#                 ar[which + j*idx] = 1
#             else:
#                 ar[which + j*idx] = 0
#
#
#     else:
#         which = idx - 1
#         count = 0
#         i = 1
#         while which+i < n and 0 <= which-i:
#             if ar[which-i] == ar[which + i]:
#                 count += 1
#                 i += 1
#             else:
#                 break
#
#         if count == 0: # 대칭이 없을 때
#             if ar[which]:
#                 ar[which] = 0
#             else:
#                 ar[which] = 1
#         else: # 대칭이 있을 때
#             if ar[which]: # 현재위치 뒤집고
#                 ar[which] = 0
#             else:
#                 ar[which] = 1
#             for c in range(1, count+1): # 대칭이 되는 만큼 뒤집기
#                 num = ar[which+c]
#                 if num:
#                     ar[which+c] = 0
#                     ar[which-c] = 0
#                 else:
#                     ar[which + c] = 1
#                     ar[which - c] = 1
#
#
# for i in range(0, len(ar),20):
#     print(*ar[i:i+20])

### swea 달팽이 숫자
# T = int(input())
#
# def solve():
#     n = int(input())
#
#     ar = [[0] * n for _ in range(n)]
#
#     direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     d = 0
#     y = x = 0
#
#     for i in range(1, n*n+1):
#         ar[y][x] = i
#
#         new_y = y+direct[d][0]
#         new_x = x+direct[d][1]
#
#         if new_y < 0 or new_y >= n or new_x < 0 or new_x >= n or ar[new_y][new_x] != 0:
#             d += 1
#             if d == 4:
#                 d = 0
#
#         y += direct[d][0]
#         x += direct[d][1]
#     return ar
#
# for t in range(1, T+1):
#     print(f'#{t}')
#     result = solve()
#     for i in result:
#         print(*i)