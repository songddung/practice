import heapq
T = int(input())

def solve(start_node):
    pq = [(0, start_node)]
    key = [float('inf')] * N
    mst = [False] * N
    result = 0

    key[start_node] = 0
    count = 0

    while pq and count < N:
        w, n = heapq.heappop(pq)

        if mst[n]:
            continue

        mst[n] = True
        result += w
        count += 1

        for next_node in range(N):
            cost = graph[n][next_node]

            if cost == 0 or mst[next_node]:
                continue
            if cost < key[next_node]:
                key[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    return result



for t in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[0] * N for _ in range(N)]
    st, end , weight = map(int, input().split())
    graph[st][end] = weight
    graph[end][st] = weight
    print(graph)
    print(f'#{t} {solve(0)}')