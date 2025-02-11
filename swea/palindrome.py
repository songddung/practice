T = int(input())

def solve():
    n, m = map(int, input().split())
    ar = []

    for _ in range(n):  # 받으면서 가로확인
        ar.append(list(input()))

    if n == m:
        for i in range(n): # 받으면서 가로확인
            if ar[i] == ar[i][::-1]:
                return ar[i]
    else:
        for i in range(n):
            for j in range(n-m+1): # 0 ~ 7
                l_line = []
                for k in range(m): # 0 ~ 12
                    l_line.append(ar[i][j+k])
                if l_line == l_line[::-1]:
                    return l_line

    for i in range(n): # 세로확인 , 열
        for j in range(n-m+1): # 행
            l_line = []
            for k in range(m):

                l_line.append(ar[j+k][i])
            if l_line == l_line[::-1]:
                return l_line




for t in range(1, T+1):
    print(f'#{t}', end=' ')
    print(*solve(), sep='')