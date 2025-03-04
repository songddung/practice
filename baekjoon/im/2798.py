# 블랙잭

N, M = map(int, input().split())
ar = list(map(int, input().split()))
arr = []
for i in ar:
    for j in ar:
        if i != j:
            for k in ar:
                if i != k and j != k:
                    if i+j+k <= M:
                        arr.append((i, j, k))

max_num = 0

for i in arr:
    if max_num < i[0]+i[1]+i[2]:
        max_num = i[0]+i[1]+i[2]

print(max_num)