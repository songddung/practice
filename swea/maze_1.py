T = 10

# 시작점 찾는 함수
def find_start(n, graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                return i, j

def solve():
    tc = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    y, x = find_start(16, graph)


    visited = [[0] * 16 for _ in range(16)]
    q = [(y, x)]
    visited[y][x] = 1

    while q:
        ti, tj = q.pop(0)
        if graph[ti][tj] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            dy, dx = ti + di, tj + dj
            if 0 <= dy < 16 and 0 <= dx < 16 and graph[dy][dx] != 1 and visited[dy][dx] == 0:
                q.append((dy, dx))
                visited[dy][dx] = visited[ti][tj] + 1

    return 0

for t in range(1, T+1):
    print(f'#{t} {solve()}')