T = int(input())

for i in range(T):
    arr = [[0] * 10 for i in range(10)]
    N = int(input())
    num = 0
    for j in range(N):
        ar = list(map(int, input().split()))
        for k in range(ar[0], ar[2]+1):
            for q in range(ar[1], ar[3] + 1):
                arr[k][q] += ar[4]

    for p in range(10):
        for o in range(10):
            if arr[p][o] == 3:
                num += 1
                # if arr[k][q] == 0:
                #     arr[k][q] = ar[-1]
                # elif arr[k][q] != 3:
                #     arr[k][q] = 3
                #     num += 1
    # for l in range(len(arr)):
    #     print(arr[l])
    print(f'#{i+1} {num}')

