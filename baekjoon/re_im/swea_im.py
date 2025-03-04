# 강사님 문제
# T = 테케
# N = 행렬의 길이
# A,B,C : 길이 1,2,3
# H : 집

my_dict = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

T = int(input())


def solve():
    N = int(input())
    ar = [list(map(str, input().strip())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # print(ar[i][j])
            if ar[i][j] in ('A', 'B', 'C'):
                for k in range(1, my_dict[ar[i][j]]+1):
                    for dy, dx in direct:
                        ni, nj = i+dy*k, j+dx*k
                        if 0 <= ni < N and 0 <= nj < N:
                            if ar[ni][nj] == 'H':
                                ar[ni][nj] = 'X'
    result = 0
    for i in range(N):
        result += ar[i].count('H')

    return result

for t in range(1, T+1):
    print(f'#{t} {solve()}')

