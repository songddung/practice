T = int(input())

def solve():
    n, m = map(int, input().split())

    ar = [list(map(int, input().split())) for _ in range(n)]
    max_num = 0
    for i in range(n): # 가로 확인
        cnt = 0
        for j in range(m):
            if ar[i][j] == 0:
                if max_num < cnt:
                    max_num = cnt
                cnt = 0
                continue
            else:
                cnt += 1
        if max_num < cnt:
            max_num = cnt

    for j in range(m): # 세로 화인
        cnt = 0
        for i in range(n):
            if ar[i][j] == 0:
                if max_num < cnt:
                    max_num = cnt
                cnt = 0
                continue
            else:
                cnt += 1
        if max_num < cnt:
            max_num = cnt
    return max_num
for t in range(1, T+1):
    print(f'#{t} {solve()}')
