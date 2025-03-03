# T = 10
#
# priority = {'+':1, '-':1, '*':2, '/': 2}
# def solve():
#     N = int(input())
#     text = input()
#     num_ar = []
#     str_ar = []
#
#     # 후위 표기식 만들기
#     for i in range(N):
#         if text[i].isdigit():
#             num_ar.append(text[i])
#             # if str_ar:
#             #     plus = str_ar.pop()
#             #     num_ar.append(plus)
#         # else:
#         #     str_ar.append(text[i])
#
#         else:
#             while str_ar and priority[str_ar[-1]] > priority[text[i]]:
#                 t = str_ar.pop()
#                 num_ar.append(t)
#             str_ar.append(i)
#
#     while str_ar:
#         num_ar.append(str_ar.pop())
#
#     # 후위 표기식 계산하기
#     stack = []
#     for i in num_ar:
#         if i.isdigit():
#             stack.append(int(i))
#         else:
#             num1 = stack.pop()
#             num2 = stack.pop()
#             if i == '+':
#                 stack.append(num1 + num2)
#             elif i == '*':
#                 stack.append(num1 * num2)
#     else:
#         return stack.pop()
# for t in range(1, T+1):
#     print(f'#{t} {solve()}')


def calcu2(arr):
    stack = []
    calc = []
    priority = {'+':1, '-':1, '*':2, '/': 2}

    # 후위 표기식으로 변환 (전부 str형태)
    for ar in arr:
        if ar.isdigit():
            calc.append(ar)
        else:
            while stack and priority[stack[-1]] > priority[ar]:
                t = stack.pop()
                calc.append(t)
                stack.append(ar)

    while stack:
        calc.append(stack.pop())
    # return calc

    # 계산 부분분
    nums = []
    for num in calc:
        if num.isdigit():
            nums.append(int(num))
        else:
            a = nums.pop()
            b = nums.pop()
            if num == '+':
                nums.append(a+b)
            elif num == '*':
                nums.append(a*b)
    return nums[0]


T = 10
for t in range(1, T + 1):
    n = int(input())
    arr = list(input())
    result = calcu2(arr)
    print(f'#{t} {result}')