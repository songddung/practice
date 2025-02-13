T = int(input())

def solve():
    n = int(input())

    base = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if base[i] != goal [i]:
            count += 1
            for j in range(i,n):
                if base[j] == 0:
                    base[j] = 1
                else:
                    base[j] = 0
    return count
for t in range(1, T+1):
    print(f'#{t} {solve()}')