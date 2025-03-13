# 베이비진

T = int(input())


def baby_gin(ar):
    for c in range(0, 10):
        if ar.count(c) >= 3:
            return True

    ar.sort()
    set_ar = set(ar)
    set_ar = list(set_ar)

    if len(set_ar) >= 3:
        for j in range(len(set_ar) - 2):
            if set_ar[j] == set_ar[j + 1] - 1 == set_ar[j + 2] - 2:
                return True


def solve():
    ar = list(map(int, input().split()))
    p1 = []
    p2 = []
    i = 1

    while ar:
        num = ar.pop(0)

        if i % 2 != 0:
            p1.append(num)

            if len(p1) >= 3:
                result = baby_gin(p1)
                if result:
                    return 1

        else:
            p2.append(num)

            if len(p2) >= 3:
                result = baby_gin(p2)
                if result:
                    return 2
        i += 1
    return 0


for t in range(1, T+1):
    print(f'#{t} {solve()}')

'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
'''