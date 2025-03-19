'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''
from collections import deque


# DFS
def dfs(node):
    print(node, end=" ")

    for nn in ar[node]:
        if visited[nn]:
            continue

        visited[nn] = 1
        dfs(nn)


# BFS
def bfs(node):
    q = deque()
    q.append(node)

    while q:
        num = q.popleft()
        print(num, end=' ')
        for nn in ar[num]:
            if not visited[nn]:
                visited[nn] = 1
                q.append(nn)


N, M = map(int, input().split())
ar = [[] for _ in range(N+1)]

for i in range(M):
    idx, v = map(int, input().split())
    ar[idx].append(v)
    ar[v].append(idx)

visited = [0] * (N + 1)
visited[1] = 1
dfs(1)

print()
visited = [0] * (N + 1)
visited[1] = 1
bfs(1)


