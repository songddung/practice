T = int(input())

def solve():
    ar = list(map(str, input().split()))
    stack = []
    top = -1
    for i in ar:
        if i.isdigit():
            top += 1
            stack.append(i)

        else:
            if top < 1:
                return 'error'
            else:
                num1, num2 = stack[top], stack[top-1]




for t in range(T, T+1):
    print(f'#{t} {solve()}')