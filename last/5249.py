# 최소 신장 트리
# 크루스칼
#   - 모든 간선들을 보면서
#   - 가중치가 작은 간선부터 고르자(정렬)
#   - 이 때, 싸이클이 발생하면 넘어감
import heapq


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    ar = []

    for _ in range(E):
        st, ed, w = map(int, input().split())
        ar.append((st, ed, w))
    ar.sort(key=lambda x: x[2])
    parents = [i for i in range(N+1)]

    cnt = 0  # 현재까지 선택한 간선 수
    result = 0  # 가중치 합

    for u, v, w in ar:
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            result += w

            if cnt == N:
                break

    print(f'#{t} {result}')
