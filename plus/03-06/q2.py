'''
3 4
1 2 3 4
5 6 7 8
9 10 11 12
'''

N, M = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]
result=[]

for j in range(M):
    lst = []
    for i in range(N-1, -1, -1):
        lst.append(ar[i][j])
    result.append(lst)

for i in result:
    print(*i)