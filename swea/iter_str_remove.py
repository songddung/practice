T = int(input())

def solve():
    txt = input()
    stack = ['']

    for i in txt:
        if i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return len(stack)-1





for t in range(1, T+1):
    print(f'#{t} {solve()}')