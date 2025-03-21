import heapq


def solve():
    dist = [float('inf')] * (N+1)
    dist[0] = 0
    pq = [(0, 0)]

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > dist[node]:
            continue

        for next_cost, next_node in ar[node]:
            new_cost = cost + next_cost

            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return dist[N]


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())  # N: 도착, M: 간선의 수
    ar = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        ar[s].append((w, e))

    print(f'#{t} {solve()}')
