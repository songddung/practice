T = int(input())


for i in range(T):
    N, M = map(int, input().split())
    ar = list(map(int, input().split()))
    max_num = sum(ar[0:M])
    min_num = sum(ar[0:M])

    for j in range(N-M+1):
        if max_num < sum(ar[j:j+M]):
            max_num = sum(ar[j:j+M])

        if min_num > sum(ar[j:j+M]):
            min_num = sum(ar[j:j+M])

    print(f'#{i+1} {max_num-min_num}')
