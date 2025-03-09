from collections import deque
import pprint
T = int(input())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(y, x, N, ar):
    q = deque()
    q.append((y,x))
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    total = ar[y][x]
    while q:
        ci, cj = q.popleft()

        for dy, dx in direct:
            ni, nj = ci + dy, cj + dx

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1

                if visited[ni][nj] <= N//2 + 1:
                    total += ar[ni][nj]
    # for i in range(len(visited)):
    #     print(visited[i])
    return total



def solve():
    N = int(input())
    ar = [list(map(int, input())) for _ in range(N)]
    y = x = N//2



    return bfs(y, x, N, ar)



for t in range(1, T+1):
    print(f'#{t} {solve()}')

