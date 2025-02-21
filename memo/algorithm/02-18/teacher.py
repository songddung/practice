
# step1 : 중위 표기를 후위표기로 바꾼다.
# ()가 없어지고 연산 순서대로 표시된다.

def step1(s):
    result = []
    STACK = []
    # priority = {'+':1, '-':1, '*':2, '/':2, '(': }
    isp = {'+':1, '-':1, '*':2, '/':2, '(':0}
    icp = {'+':1, '-':1, '*':2, '/':2, '(':3}
    for c in s:
        if c.isdigit():
            result.append(c)
        # elif c == '(':
        #     STACK.append(c)
        elif c == ')':
            while STACK and STACK[-1] != '(':
                result.append(STACK.pop(-1))
            STACK.pop(-1)
        else:
            # pre = STACK[-1]
            if not STACK or isp[STACK[-1]] < icp[c]:
                STACK.append(c)
            else:
                # print(STACK, c)
                while STACK and isp[STACK[-1]] >= icp[c]:
                    result.append(STACK.pop(-1))
                STACK.append(c)
    while STACK:
        result.append(STACK.pop(-1))

    # print(result)
    return result

def cal(op1, op2, ope):
    if ope == '+':
        return op1+op2
    if ope == '-':
        return op2-op1
    if ope == '*':
        return op1*op2
    if ope == '/':
        return op2//op1

# 후위 표기법으로 만들어진 리스트를 가지고 계산 결과를 return
def step2(lst):
    STACK = [] # 정수만
    for c in lst:
        if c.isdigit():
            STACK.append(int(c))
        else:
            value1 = STACK.pop(-1)
            value2 = STACK.pop(-1)
            STACK.append(cal(value1, value2, c))

    return STACK.pop(-1)


s = '(6+5*(2-8)/2)'
post_order = step1(s)
print(step2(post_order))

s = '2*4+3'
post_order = step1(s)
print(step2(post_order))

s = '2*4+(3-2)'
post_order = step1(s)
print(step2(post_order))