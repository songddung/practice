# a = [2,4,7]
# bit = [0]*3
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             # print(bit)
#             s = 0
#             for b in range(3):
#                 if bit[b]:
#                     print(a[b], end=' ')
#                     s += a[b]
#             print(bit, s)
#_
#
# print(bin(7)[2:])

arr = [1,2,3,4,5,6,7,8,9,10,11,12]

T = int(input())
for q in range(1, T+1) :
    N, K = map(int,input().split())
    n = len(arr)
    count = 0
    for i in range(1<<n):
        ar = []
        for j in range(n):
            if i & (1<<j):
                ar.append(arr[j])
        if len(ar) == N and sum(ar) == K:
            count += 1


    print(f'#{q} {count}')