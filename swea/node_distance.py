T = int(input())


def bfs(start, end, graph):
    q = [start]
    visited = set([start])
    dist = {start: 0}

    while q:
        curr = q.pop(0)

        if curr == end:
            return dist[curr]

        for next_node in graph[curr]:
            if next_node not in visited:  # 방문 확인
                visited.add(next_node)  # 방문 처리
                q.append(next_node)  # 큐에 넣고
                dist[next_node] = dist[curr]+1  # 거리 갱신

    return 0


def solve():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for i in range(e):
        idx , value = map(int, input().split())
        graph[idx].append(value)
        graph[value].append(idx)


    start , end = map(int, input().split())
    return bfs(start, end, graph)



for t in range(1, T+1):
    print(f'#{t} {solve()}')