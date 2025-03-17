# 이진 탐색

T = int(input())


def solve(check, start, end, d):
    global count
    m = (start+end)//2

    if start > end:
        return

    if A[m] == check:
        count += 1
        return

    elif A[m] < check:
        s = m + 1
        if d == '우':
            return
        d = '우'
        solve(check, s, end, d)

    elif A[m] > check:
        e = m - 1
        if d == '좌':
            return
        d = '좌'
        solve(check, start, e, d)

sorted()
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    count = 0
    for i in B:
        start = 0
        end = len(A)-1
        dir = 0
        solve(i, start, end, dir)

    print(f'#{t} {count}')

'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5

'''