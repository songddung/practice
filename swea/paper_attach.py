T = int(input())

def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return solve(n-1) + 2 * solve(n-2)


for t in range(1, T+1):
    n = int(input())/10
    print(f'#{t} {solve(n)}')