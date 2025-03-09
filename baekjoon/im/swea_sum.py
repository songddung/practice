T = 10


def solve():
    tc = int(input())
    ar = [list(map(int,input().split())) for _ in range(100)]
    row = 0
    col = 0
    diagonal = 0
    diagonal_r = 0

    for i in range(100):
        count = sum(ar[i])
        row = max(row, count)

    # 행열 변경 후 기존의 열 검사
    r_ar = list(map(list, zip(*ar)))
    for i in range(100):
        count = sum(r_ar[i])
        col = max(col, count)

    # 대각선 검사
    count = 0
    for i in range(100):
        count += ar[i][i]
        diagonal = max(count, diagonal)

        r_count = ar[i][99-i]
        diagonal_r = max(diagonal_r, r_count)

    return max(row, col, diagonal_r, diagonal)
for t in range(1, T+1):
    print(f'#{t} {solve()}')