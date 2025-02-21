# 7 8
# 4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7

def bfs(s, V):
    visited = [0] * (V+1)  # visited 생성
    q = []
    q.append(s)  # 시작점 인큐
    visited[s] = 1
    while q:
        t = q.pop(0)  # 디큐해서 t에 저장
        print(t)  # t정점에 대한 처리
        for w in adj_l[t]:  # t에 인접한 정점 w 중, 인큐되지 않는 정점이 있으면
            if visited[w] == 0:
                q.append(w)  # 인큐, 인큐표시
                visited[w] = visited[t] + 1
    print(visited)

n, m = map(int, input().split())
ar = list(map(int, input().split()))

adj_l = [[] for _ in range(n + 1)]
for i in range(m):
    v1, v2 = ar[i*2], ar[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)



bfs(5,7)