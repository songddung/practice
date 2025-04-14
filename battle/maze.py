from collections import deque

T = 10
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(st, end, lst):
    q = deque()
    visited = [[0] * 16 for _ in range(16)]
    visited[st[0]][st[1]] = 1
    q.append(st)


    while q:

        ci, cj = q.popleft()
        if end == (ci, cj):
            return 1
        for dy, dx in direct:
            ny, nx = ci + dy, cj + dx
            if 0 <= ny < 16 and 0 <= nx < 16 and visited[ny][nx] == 0 and lst[ny][nx] != 1:
                q.append((ny, nx))
                visited[ny][nx] = 1
    # for i in range(16):
    #     print(visited[i])
    return 0



def solve():
    tc = input()
    ar = [list(map(int, input())) for _ in range(16)]
    start = None
    end = None
    for i in range(16):

        if 2 in ar[i]:
            start = (i, ar[i].index(2))
            # print(start)

        if 3 in ar[i]:
            end = (i, ar[i].index(3))
            # print(end)

        if start and end:
           break
    # if not start or not end:
    #     return 0

    result = bfs(start, end, ar)

    return result


for t in range(1, T+1):
    print(f'#{t} {solve()}')