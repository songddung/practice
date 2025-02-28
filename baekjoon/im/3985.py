# 롤케이크

L = int(input())
N = int(input())
ar = [0 for _ in range(L+1)]

max_num = 0 # 예측
midx = 0 # 예측
idx = 0 # 실제
mx = 0 # 실제
for i in range(1, N+1):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    if max_num < e-s:
        max_num = e-s
        midx = i

    for j in range(s,e+1):
        if ar[j] == 0:
            ar[j] = i

for i in range(1, N+1):
    if ar.count(i) > mx:
        mx = ar.count(i)
        idx = i
print(midx, idx)