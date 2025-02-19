T = 10

def solve():
    N = int(input())
    ar = list(map(int, input().split()))
    i = 1
    while True:
        if i == 6:
            i = 1

        num = ar.pop(0) - i
        if num <= 0:
            ar.append(0)
            return ar
        ar.append(num)
        i += 1

    return ar


for t in range(1, T+1):
    print(f'#{t}', *solve())