T = int(input())

def solve():
    n = int(input())
    base = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    count = 0

    for i in range(len(base)):
        if goal[i] == base[i]:
            continue
        else:
            count += 1
            for j in range(len(base)-i):
                if base[i+j] == 1:
                    base[i + j] = 0
                else:
                    base[i + j] = 1
    return count
for t in range(1, T+1):
    print(f'#{t} {solve()}')