N = 10


for i in range(1, N+1):
    sum_num_d = 0
    sum_num_d2 = 0
    sum_num_c = 0
    sum_num_r = 0
    sum_list = []
    arr = []
    idx = int(input())
    for j in range(100):
        arr.append(list(map(int, input().split())))

    for k in range(100):
        for p in range(100):
            sum_num_c += arr[k][p]
            sum_num_r += arr[p][k]
        sum_list.append(sum_num_c)
        sum_list.append(sum_num_r)
        sum_num_c = 0
        sum_num_r = 0

    for o in range(100):
        sum_num_d2 += arr[o][o]
        sum_num_d += arr[o][99-o]

    sum_list.append(sum_num_d)
    sum_list.append(sum_num_d2)
    max_num = 0

    for ii in range(len(sum_list)):
        if sum_list[ii] > max_num:
            max_num = sum_list[ii]
    print(f'#{i} {max_num}')
