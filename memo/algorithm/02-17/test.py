# stack = [0]*100
# top = -1
# icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
# isp = {'(':0, '*':2, '/':2, '+':1, '-':1}
#
# fx = '(6+5*(2-8)/2)'
# susik = ''
# for x in fx:
#     if x not in '(+-*/)':   # 피연산자
#         susik += x
#     elif x == ')':      # '('까지 pop()
#         while stack[top] != '(':    # peek
#             susik += stack[top]
#             top -= 1
#         top -= 1        # '(' 버림. pop
#     else:   # '(+-*/'
#         if top==-1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
#             top += 1    # push
#             stack[top] = x
#         elif isp[stack[top]] >= icp[x]:
#             while top > -1 and isp[stack[top]] >= icp[x]:
#                 susik += stack[top]
#                 top -= 1
#             top += 1  # push
#             stack[top] = x
#
# print(susik)
#
# #susik = '6528-*2/+'
# for x in susik:
#     if x not in '+-/*': # 피연산자면...
#         top += 1            # push(x)
#         stack[top] = int(x)
#     else:
#         op2 = stack[top]  # pop()
#         top -= 1
#         op1 = stack[top]  # pop()
#         top -= 1
#         if x=='+':  # op1 + op2
#             top += 1                # push()
#             stack[top] = op1 + op2
#         elif x=='-':
#             top += 1
#             stack[top] = op1 - op2
#         elif x=='/':
#             top += 1
#             stack[top] = op1 / op2
#         elif x=='*':
#             top += 1
#             stack[top] = op1 * op2
#
# print(stack[top])



ar = [[0]*1001 for _ in range(1001)]

num = int(input())

for n in range(1, num+1):
    s2, s1, l2, l1 = map(int, input().split())

    for i in range(s1, s1+l1):
        ar[i][s1:s1+l1] = [n] * l2

for n in range(1, num+1):
    t = 0
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j] == n:
                t += 1
    if t :
        print(t)
    else:
        print(0)