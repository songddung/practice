T = int(input())

for i in range(T):
    N = int(input())
    ar = [0] * 10
    arr = list(map(int, input()))
    idx = 0
    max_num = 0

    for j in arr:
        ar[j] += 1
    for j in range(len(ar)):
        if ar[j] >= max_num:
            max_num = ar[j]
            idx = j

    print(f'#{i+1} {idx} {max_num}')


