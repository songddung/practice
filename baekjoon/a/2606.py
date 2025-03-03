# 바이러스
# 입력1 : node 수
# 입력2 : 간선 수



N = int(input())
G = int(input())
ar = [[] for _ in range(N+1)]

for i in range(G):
    idx, v = map(int,input().split())
    ar[idx].append(v)  # 방향 잘보고 넣기 단방향일때, 양방향일때 구분!!
    ar[v].append(idx)

stack = [1]
visited = [1]
count = 0
while stack:

    n = stack.pop()
    for i in range(len(ar[n])):
        if ar[n][i] not in visited:
            stack.append(ar[n][i])
            visited.append(ar[n][i])
            count += 1

print(count)