# # 빙산
# # 4방향을 탐색해 0과 마주하고 있는 면의 갯수만큼 차감
from collections import deque

direct = ((-1, 0), (0, 1), (1, 0), (0, -1))


def bfs():
    visited = [[False] * m for _ in range(n)]
    t = 0

    for i in range(n):
        for j in range(m):
            if ar[i][j] != 0 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True

                while q:
                    y, x = q.popleft()

                    for k in range(4):
                        dy, dx = y + direct[k][0], x + direct[k][1]

                        if 0 <= dy < n and 0 <= dx < m and not visited[dy][dx]:
                            if ar[dy][dx] != 0:
                                q.append((dy, dx))
                                visited[dy][dx] = True

                t += 1

                if t >= 2:
                    return t

    return t


def test():
    global ar

    arr = [row[:] for row in ar]

    for i in range(n):
        for j in range(m):
            if ar[i][j] != 0:
                c = 0

                for k in range(4):
                    dy, dx = i + direct[k][0], j + direct[k][1]

                    if 0 <= dy < n and 0 <= dx < m and ar[dy][dx] == 0:
                        c += 1

                arr[i][j] = max(0, ar[i][j] - c)

    ar = arr


def main():
    global ar, n, m

    n, m = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(n)]

    i = 0

    while True:
        r = bfs()

        if r >= 2:
            print(i)
            return
        elif r == 0:
            print(0)
            return

        test()
        i += 1


if __name__ == "__main__":
    main()
