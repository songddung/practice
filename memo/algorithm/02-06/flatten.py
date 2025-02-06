test = 10

for i in range(test):

    N = int(input())
    ar = list(map(int, input().split()))


    while N > 0:
        max_num = 0
        min_num = ar[0]
        max_idx = 0
        min_idx = 0
        for j in range(len(ar)):
            if max_num < ar[j]:
                max_idx = j
                max_num = ar[j]
            if min_num > ar[j]:
                min_idx = j
                min_num = ar[j]

        ar[max_idx] -= 1
        ar[min_idx] += 1
        N -= 1

        if (max_num - min_num) <= 1:
            print(f'#{i+1} {max_num-min_num}')
            break

    max_num = 0
    min_num = ar[0]
    max_idx = 0
    min_idx = 0
    for j in range(len(ar)):
        if max_num < ar[j]:
            max_idx = j
            max_num = ar[j]
        if min_num > ar[j]:
            min_idx = j
            min_num = ar[j]
    print(f'#{i+1} {ar[max_idx]-ar[min_idx]}')