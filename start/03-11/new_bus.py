T = int(input())


def solve():
    N = int(input())
    ar = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for i in ar:
        mx = max(mx, max(i))
    bus_stop = [0] * (mx+1)

    for i in ar:
        ty, a, b = i

        if ty == 1:
            for j in range(a, b + 1):
                bus_stop[j] += 1

        elif ty == 2:
            if a % 2 == 0:
                for j in range(a, b + 1):
                    if j % 2 == 0:
                        bus_stop[j] += 1
            else:
                for j in range(a, b + 1):
                    if j % 2:
                        bus_stop[j] += 1
        else:
            if a % 2 == 0:
                for j in range(a, b + 1):
                    if j % 4 == 0:
                        bus_stop[j] += 1
            else:
                for j in range(a, b + 1):
                    if j % 3 == 0 and j % 10:
                        bus_stop[j] += 1
    # print(bus_stop)/
    return max(bus_stop)


for t in range(1, T + 1):
    print(f'#{t} {solve()}')
