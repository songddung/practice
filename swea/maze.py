T = int(input())

def solve():
    n = int(input())
    ar = [list(map(int, input().strip())) for _ in range(n)]

    for row in range(n):
        if ar[row].count(2):
            col = ar[row].index(2)
            break

    STACK = []
    visited = [[0] * n for _ in range(n)]

    STACK.append((row, col))
    visited[row][col] = 1
    while STACK:
        cur_r, cur_c = STACK.pop()

        for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_y = cur_r + dy
            new_x = cur_c + dx
            if 0 <= new_y < n and 0 <= new_x < n and not visited[new_y][new_x]:
                if ar[new_y][new_x] == 0:
                    STACK.append((new_y, new_x))
                    visited[new_y][new_x] = 1
                elif ar[new_y][new_x] == 3:
                    return 1

    return 0



for t in range(1, T+1):
    print(f'#{t} {solve()}')