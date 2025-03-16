T = int(input())


def solve():
    N = int(input())
    ar = [[] for _ in range(N+1)]
    for _ in range(N-1):
        idx, v = map(int, input().split())
        ar[idx].append(v)
    check = list(map(int, input().split()))
    my_ar = []

    for c in check:
        arr = [c]
        while True:
            for i in range(len(ar)):
                if ar[i]:
                    if c in ar[i]:
                        arr.append(i)
                        c = i
                        break
            else:
                my_ar.append(arr)
                break

    for i in range(len(my_ar[0])):
        for j in range(len(my_ar[1])):
            if my_ar[0][i] == my_ar[1][j]:
                return my_ar[0][i]


for t in range(1, T+1):
    print(solve())