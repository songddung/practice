# T = int(input())
#
# def solve():
#     txt = input()
#     stack = [0] * len(txt)
#     top = -1
#     for i in txt:
#         # print(i)
#         if i == '}':
#             if stack and stack[top] == '{':
#                 stack.pop(top)
#                 top -= 1
#             else:
#                 top += 1
#                 stack[top] = i
#
#         elif i == ')':
#             if stack and stack[top] == '(':
#                 stack.pop(top)
#                 top -= 1
#             else:
#                 top += 1
#                 stack[top] = i
#
#
#         else:
#             if i == '{' or i == '(':
#                 top += 1
#                 stack[top] == i
#
#         print(top)
#
#
# for t in range(1, T+1):
#     print(f'#{t} {solve()}')


T = int(input())

def solve():
    txt = input()
    stack = []
    for i in txt:
        if i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)

        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

        else:
            if i == '{' or i == '(':
                stack.append(i)

    # 스택에 남아있는 괄호의 개수
    top = len(stack)
    if top != 0:
        return 0
    else:
        return 1

for t in range(1, T + 1):
    print(f'#{t} {solve()}')
