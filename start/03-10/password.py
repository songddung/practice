T = int(input())


def solve():
    N, K = map(int, input().split())
    ar = list(map(str, input()))
    my_set = set()
    jump = N // 4
    for i in range(jump):
        num = ar.pop()
        ar.insert(0, num)

        for j in range(0, N, jump):
            check = ar[j:j+jump]
            txt = ''
            for k in check:
                txt += k

            my_set.add(int(txt, 16))
    sorted_set = sorted(my_set, reverse=True)
    return sorted_set[K-1]





for t in range(1, T+1):
    print(f'#{t} {solve()}')