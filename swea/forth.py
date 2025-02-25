# T = int(input())
#
#
# def solve():
#     ar = list(map(str, input().split()))
#     stack = [0] * len(ar)
#     top = -1
#     for i in ar:
#         if i.isdigit():
#             top += 1
#             stack[top] = int(i)
#         else:
#             if i == '.':
#                 return stack[top]
#             if top < 1:
#                 return 'error'
#             else:
#
#                 num1, num2 = int(stack[top]), int(stack[top-1])
#                 top -= 1
#                 if i == '+':
#                     stack[top] = num1 + num2
#                 elif i == '*':
#                     stack[top] = num1 * num2
#                 elif i == '/':
#                     stack[top] = num1 // num2
#                 elif i == '-':
#                     stack[top] = num1 - num2
#
#
#
#
# for t in range(1, T+1):
#     print(f'#{t} {solve()}')
T = int(input())

def solve():
    ar = list(map(str, input().split()))
    stack = []
    for i in ar:
        if i.isdigit():
            stack.append(int(i))
        elif i == '.':
            if len(stack) != 1:
                return 'error'  # 결과가 정확히 하나인지 확인
            return stack.pop()
        else:
            if len(stack) < 2:
                return 'error'  # 피연산자가 충분하지 않음
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':
                stack.append(num1 + num2)
            elif i == '-':
                stack.append(num1 - num2)
            elif i == '*':
                stack.append(num1 * num2)
            elif i == '/':
                if num2 == 0:
                    return 'error'  # 0으로 나누기
                stack.append(num1 // num2)

for t in range(1, T + 1):
    print(f'#{t} {solve()}')
