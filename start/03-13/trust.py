# 신뢰

T = int(input())


def solve():
    N, *ar = map(str, input().split())
    B_ar = []
    O_ar = []
    b = 1
    o = 1
    time = 0
    time_b = 0
    time_o = 0

    for i in range(0, len(ar), 2):
        if ar[i] == "B":
            B_ar.append(ar[i+1])
        else:
            O_ar.append(ar[i+1])

    for i in B_ar:
        time_b += abs(b-int(i)) + 1
        b = int(i)
        time = max(time, time_b)

    for i in O_ar:
        time_o += abs(o-int(i)) + 1
        o = int(i)
        time = max(time, time_o)

    return time


for t in range(1, T+1):
    print(f'#{t} {solve()}')


'''
3
4 B 2 O 1 O 2 B 4
3 B 5 B 8 O 100
2 O 2 O 1
'''
