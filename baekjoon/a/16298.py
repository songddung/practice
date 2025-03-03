 # 뱀과 사다리게임
 # 1차원 배열
 # 1~100까지
 # 주사위 1~6까지
 # 방탐대신 주사위 숫자만큼 더하기
 # BFS

from collections import deque
N, M = map(int, input().split())
ar = list(range(1,101))
visited = [0]*101
q = deque()
q.append(1)
visited[1] = 1
jump = []

for _ in range(N+M):
    s, e = map(int, input().split())
    jump.append((s, e))

def bfs():
    while q:
        which = q.popleft()

        for k in (which+1, which+2, which+3, which+4, which+5, which+6):

            for i in range(N + M):

                if k == jump[i][0]:
                    k = jump[i][1]
                    break
            if which == 100:
                return visited[which] - 1

            if 0 <= k < 101 and visited[k] == 0:
                q.append(k)
                visited[k] = visited[which]+1
print(bfs())

