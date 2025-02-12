T = int(input())

def solve():
    n, m = map(int, input().split())

    ar = [list(map(int, input().split())) for _ in range(n)]

    max_num = 0
    for i in range(n):
        for j in range(m):
            num = ar[i][j]
            for k in range(1, num+1):
                if 0 <= i - k < n:
                    num += ar[i - k][j]  # 위쪽
                if 0 <= j + k < m:
                    num += ar[i][j + k]  # 오른쪽
                if 0 <= j - k < m:
                    num += ar[i][j - k]  # 왼쪽
                if 0 <= i + k < n:
                    num += ar[i + k][j]  # 아래쪽

            if max_num < num:
                max_num = num
    return max_num
for t in range(1, T+1):
    print(f'#{t} {solve()}')