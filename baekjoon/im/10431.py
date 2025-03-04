# 줄세우기

n = int(input())

for _ in range(n):
    tc , *ar = map(int, input().split())
    count = 0

    for i in range(len(ar)-1, 0, -1):
        for j in range(i):
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
                count +=1
    print(f'{tc} {count}')