n, m = map(int, input().split())
ar = list(map(int, input().split()))
max_num = 0


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            if ar[i]+ar[j]+ar[k] > m:
                continue
            max_num = max(max_num, ar[i]+ar[j]+ar[k])

print(max_num)