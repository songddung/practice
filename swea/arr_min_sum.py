T = int(input())
def f(i, N, s):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global mn
    global count
    count += 1
    if i == N:  #
        if mn > s:
            mn = s
    elif mn < s:
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]  # 자리교환
            f(i+1, N, s+ar[i][p[i]])   # i+1자리 결정
            p[i], p[j] = p[j], p[i]  # 원상복구




for t in range(1, T+1):
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]
    mn = 10000
    count = 0
    f(0, N, 0)
    print(f'#{t} {mn}')
