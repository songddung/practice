T = 10
def solve():

    n = int(input())
    txt = input()
    stack = []
    open_bracket = '([{<'
    close_bracket = ')]}>'
    for i in txt:
        if i in close_bracket:
            idx = close_bracket.find(i)
            if stack and stack[-1] == open_bracket[idx]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if len(stack):
        return 0
    else:
        return 1

for t in range(1, T + 1):
    print(f'#{t} {solve()}')
