def solve():
    r_diagonal = diagonal = 0

    for i in range(N):
        if check != sum(ar[i]):
            return 'NO'
        if check != sum(r_ar[i]):
            return 'NO'
        diagonal += ar[i][i]
        r_diagonal += ar[i][N-i-1]

    if check != diagonal:
        return 'NO'
    if check != r_diagonal:
        return 'NO'

    return 'YES'


N = int(input())
ar = [list(map(int, input().split())) for _ in range(N)]
r_ar = list(map(list, zip(*ar)))

check = sum(ar[0])


print(solve())