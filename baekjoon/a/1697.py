# 숨바꼭질
# input : 현재위치 , 목표위치
# bfs로 최단거리처럼 풀기
# 방탐대신 이동넣기


start, end = map(int, input().split())
visited = [0] * 100001
visited[start] = 1
q = [start]
def bfs():
    while q:
        which = q.pop(0)
        if which == end:
            return visited[which] - 1

        for i in (which + 1, which - 1, which*2):
            if 0 <= i < 100001 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[which] + 1

print(bfs())