'''
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
3
1 1 3 3
2 2 3 4
1 3 4 5
'''

N, M = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

for i in range(Q):
    total = 0
    si, sj, ei, ej = map(int, input().split())
    si -= 1
    ei -= 1
    sj -= 1
    ej -= 1

    for j in range(si, ei+1):
        total += sum(ar[j][sj:ej+1])

    print(total)





# def total(arr):


#     for a in range(x1 - 1, x2):
#         for b in range(y1 - 1, y2):
#             sumv += arr[a][b]
#     return sumv
#
#
#
#
#
# q = int(input())
# for _ in range(q):
#     x1, y1, x2, y2 = list(map(int, input().split()))
#     result = total(arr)
#     print(result)