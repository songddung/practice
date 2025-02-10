T = int(input())

def solve():
    n = int(input())
    arr = [[-1]*n for _ in range(n)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0

    row = col = 0
    value = 1
    for i in range(1, n*n+1):
        arr[row][col] = i

        newR = row + delta[d][0]
        newC = col + delta[d][1]
        if newR < 0 or newR >= n or newC < 0 or newC >= n or arr[newR][newC] != -1:
            d += 1
            if d == 4:
                d = 0
        row += delta[d][0]
        col += delta[d][1]
    return arr
for t in range(1,T+1):
    result = solve()

    print(f'#{t}')
    for i in range(len(result)):
        print(*result[i], sep=' ')