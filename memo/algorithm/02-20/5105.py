T = int(input())


# 시작점 찾는 함수
def find_start(n, maze):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j


def solve():
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    y, x = find_start(n, maze)  # 시작점 받기

    visited = [[0] * n for _ in range(n)]  # 방문여부 확인 리스트
    q = []  # 큐 생성
    q.append([y, x])  # 시작점 인큐
    visited[y][x] = 1  # 시작점 인큐 표시

    while q:
        ti, tj = q.pop(0)  # t 디큐
        if maze[ti][tj] == 3:  # t 에서 할일 출구에 도착하면 1 아니면 0
            # return 1  #
            return visited[ti][tj] - 2
        # t 인접 w 중, 인큐 되지 않은 곳이면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            dy, dx = ti + di, tj + dj
            if 0 <= dy < n and 0 <= dx < n and maze[dy][dx] != 1 and visited[dy][dx] == 0:
                q.append([dy, dx])
                visited[dy][dx] = visited[ti][tj] + 1
        # 인큐, 표시
    return 0

for t in range(1, T+1):
    print(f'#{t} {solve()}')