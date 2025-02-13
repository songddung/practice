T = 10

def solve():
    n, num = list(map(str, input().split()))
    stack = []

    for i in range(len(num)):
        if stack and num[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(num[i])
    return stack

for t in range(1,T+1):
    print(f'#{t}', end=' ')
    print(*solve(), sep='')