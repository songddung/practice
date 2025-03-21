# 하나로
# 최소의 간선 수 or 최소비용 : MST
# Prim
import heapq


def prim(tax):
    pq = [(0, 0)]  # (비용 ,노드) 형태로 저장
    visited = [0] * N  # 방문 여부 기록
    min_cost = 0  # 최소 비용

    dists = [float('inf')] * N  # 최소 비용 저장 리스트
    dists[0] = 0  # 시작점은 0

    while pq:
        # cost가 가장 저렴한 후보부터 나온다
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        # node로 가는 간선을 확정짓는 코드
        visited[node] = 1
        min_cost += cost

        for n_node in range(N):
            if visited[n_node]:
                continue

            # ((x 좌표 차이 ** 2) + (y 좌표 차이 ** 2)) * tax
            new_cost = ((x_list[n_node] - x_list[node]) ** 2 + (y_list[n_node] - y_list[node]) ** 2) * tax

            if new_cost < dists[n_node]:
                dists[n_node] = new_cost
                heapq.heappush(pq, (new_cost, n_node))

    return round(min_cost)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    result = prim(tax)
    print(f'#{t} {result}')
