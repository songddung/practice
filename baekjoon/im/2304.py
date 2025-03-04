# 창고다각형
n = int(input())
ar = [0] * 1001

max_num = 0
max_idx = 0
for _ in range(n):
    l, h = map(int,input().split())
    if max_num < h:
        max_num = h
        max_idx = l

    ar[l] = h
    

count = 0
mx = 0

for i in range(1, max_idx+1):
    if mx < ar[i]:
        mx = ar[i]
    count += mx
    

mx = 0
for i in range(len(ar)-1 , max_idx, -1):
    if mx < ar[i]:
        mx = ar[i]
    count += mx

print(count)



