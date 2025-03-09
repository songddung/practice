T = int(input())


def solve():
    a, b, c = map(int, input().split())
    if c < 3:
        return -1

    if a < b < c:
        return 0

    count = 0

    while a >= b or b >= c:
        if b >= c:
            b -= 1
            count += 1

        if a >= b:
            a -= 1
            count += 1

        if a < 1 or b < 1 or c < 1:
            return -1

        if a < b < c:
            return count



for t in range(1, T+1):
    print(f'#{t} {solve()}')