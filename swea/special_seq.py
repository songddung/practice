T = int(input())

def solve():
    n = int(input())
    ar = list(map(int, input().split()))
    arr = []

    for i in range(n//2):
        max_num = 0
        if len(ar) > 0 :
            min_num = ar[0]
        for j in range(len(ar)):
            if ar[j] < min_num:
                min_num = ar[j]

            if ar[j] > max_num:
                max_num = ar[j]

        ar.remove(max_num)
        ar.remove(min_num)

        arr.append(max_num)
        arr.append(min_num)

    return arr[0:10]

for t in range(1, T+1):
    result = solve()
    print(f'#{t}', end=' ')
    print(*result)
