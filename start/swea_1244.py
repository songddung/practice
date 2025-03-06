T = int(input())


def solve():
    arr, N = map(str, input().split())
    ar = []
    N = int(N)
    cnt = 0
    for i in arr:
        ar.append(i)

    for i in range(len(ar)-1):
        if cnt == N:
            return ar
        max_idx = i
        for j in range(i+1, len(ar)):
            if ar[j] > ar[max_idx]:
                max_idx = j
        ar[i] , ar[max_idx] = ar[max_idx], ar[i]
        cnt += 1

for t in range(1, T+1):
    print(f'#{t} {solve()}')