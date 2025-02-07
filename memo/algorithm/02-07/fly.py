

N = int(input())

for i in range(1, N+1):
    step = []
    arr = []
    N, M = map(int,input().split())
    for m in range(M):
        for t in range(M):
            if m == 0 and t == 0:
                pass
            else:
                step.append([m, t])

    for j in range(N):
        arr.append(list(map(int, input().split())))
    sum_list = []
    max_num = 0
    for k in range(N):
        for p in range(N):
            sum_n = arr[k][p]
            for ks, ps in step:
                ki = k+ks
                pi = p+ps
                if 0 <= ki < N and 0 <= pi < N:
                    sum_n += arr[ki][pi]
            if max_num < sum_n:
                max_num = sum_n
            sum_n = 0
    # max_num = 0
    # for q in range(len(sum_list)):
    #     if max_num < sum_list[q]:
    #         max_num = sum_list[q]
    print(f'#{i} {max_num}')