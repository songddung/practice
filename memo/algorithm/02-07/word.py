T = int(input())

for t in range(1, T+1):
    arr = []
    result = 0
    N, K = map(int, input().split())

    for j in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N): # 행
        num = 0
        for j in range(N): # 열
            if arr[i][j]: # 1이면
                num += 1 # 카운트 증가
            else:
                if num == K:
                    result += 1
                num = 0
        if num == K:
            result += 1


    for j in range(N):
        num = 0
        for i in range(N):
            if arr[i][j]:  # 1이면
                num += 1  # 카운트 증가
            else:
                if num == K:
                    result += 1
                num = 0
        if num == K:
            result += 1
    print(f'#{t} {result}')




    # for p in range(len(arr)):
    #     print(arr[p])
    # print()