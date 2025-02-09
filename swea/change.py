money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

def solve():
    N = int(input())
    result = []
    for i in range(len(money)):
        if N % money[i] < money[i]:
            result.append(N // money[i])
            N %= money[i]
        else:
            continue

    return result

for t in range(1,T+1):
    print(f'#{t}')
    print(*solve(), sep=" ")