# swea 연산
from collections import deque
T = int(input())


def calc(n, i):
    if i == 0:
        return n+1
    elif i == 1:
        return n - 1
    elif i == 2:
        return n*2
    elif i == 3:
        return n - 10


def solve(start, end,  cnt):
    q = deque()
    q.append((start, cnt))
    visited.add(start)
    while q:
        num, count = q.popleft()
        if num == end:
            return count
        for i in range(4):
            calc_num = calc(num, i)
            if calc_num not in visited:
                if 0 <= calc_num and calc_num - M <= 10:
                    q.append((calc_num, count+1))
                    visited.add(calc_num)


for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = set()
    print(f'#{t} {solve(N, M, 0)}')

'''
3
2 7
3 15
36 1007
'''