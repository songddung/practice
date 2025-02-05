N = 10
num = 0
for i in range(N):
    N2 = int(input())
    T = list(map(int, input().split()))

    for j in range(2, N2-2):
        if T[j] > T[j-1] and T[j] > T[j-2] and T[j] > T[j+1] and T[j] > T[j+2]:
            num += T[j] - max(T[j-1], T[j-2], T[j+1], T[j+2])

    print(f'#{i+1} {num}')
    num = 0