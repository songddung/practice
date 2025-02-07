### 최빈수 구하기
### 1000명


N = int(input())
for i in range(N):
    j = int(input())
    ar = list(map(int, input().split()))
    arr = [0]*101
    for n in ar:
        arr[n] += 1

    max_num = 0
    max_idx = 0
    for k in range(len(arr)):
        if arr[k] >= max_num:
            max_num = arr[k]
            max_idx = k

    print(f'#{j} {max_idx}')