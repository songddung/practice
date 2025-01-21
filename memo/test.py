n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_num = 0

for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            if arr[i] + arr[j] + arr[k] > m :
                continue
            else :
                ### max(arg1, arg2)
                # arg1과 arg2를 비교하여 큰 값을 리턴
                max_num = max(max_num, arr[i] + arr[j] + arr[k])
            
print(max_num)