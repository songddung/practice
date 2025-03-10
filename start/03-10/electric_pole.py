# 전봇대
# 전선 N개
# 몇 개 발생하는 지  count
# 풀이
#   기존 선과 비교
#       시작점이 높으며, 도착점이 낮음
#       시작점이 낮고, 도착점이 높음

T = int(input())


def solve():
    N = int(input())
    ar = []
    count = 0
    for i in range(N):
        A, B = map(int, input().split())
        if ar:
            for ai, bi in ar:
                if A > ai and B < bi:
                    count += 1
                if A < ai and B > bi:
                    count += 1
        ar.append((A, B))
    return count



for t in range(1, T+1):
    print(f'#{t} {solve()}')

'''
2
3
1 10
5 5
7 7
2
1 1
2 2
'''