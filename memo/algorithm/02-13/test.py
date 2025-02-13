# stack
# def my_stack():
#     top = -1
#     stack = [0] * 10
#
#     top += 1
#     stack[top] = 1
#
#     top += 1
#     stack[top] = 2
#
#     top += 1
#     stack[top] = 3
#
#     top -= 1
#     print(stack[top+1])
#
#     top -= 1
#     print(stack[top + 1])
#
#     top -= 1
#     print(stack[top + 1])
#
#
# my_stack()

# ### 연습문제 2
#
# txt = input()
#
# top = -1
# stack = [0] * 100
#
# result = 1 # 짝이 맞다고 가정
#
# for x in txt:
#     if x == '(':  # 여는 괄호면 push
#         top += 1
#         stack[top] = x
#     elif x == ')':  # 닫는 괄호인 경우
#         if top == -1:
#             result = 0
#             break
#         else:
#             top -= 1
#             # 여는 소괄호만 있으므로 비교 작업 생략
#
# else:
#     # 여는 괄호가 남아있으면
#     if top > -1:
#         result = 0
# print(result)
#
# ### 피보나치
# def fibo(n):
#     global cnt
#     cnt += 1
#     if n < 2:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)
# cnt = 0
# print(fibo(10), cnt)

## 모든 배열 원소 접근
arr = [1,2,3]
def f(i,n):
    if i == n:
        return
    else:
        print(arr[i])
        f(i+1,n)
# f(0,1000)

### 배열에v가 있으면 1. 없으면 0
v = int(input())
def f2(i,n,v):
    if i == n:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return f2(i+1,n,v)

print(f2(0,3,v))


# import math
# print(math.factorial(10000))

### 강사님 설명
def push(value):
    global top

    if not is_full():
        top += 1
        STACK[top] = value
    else:
        print('full')

def pop():
    global top

    if not is_empty():
        value = STACK[top]
        top -= 1
        return value
    else:
        print('빔')

def is_full():
    return top == SIZE -1


def is_empty():
    if top == -1:
        return True
    else:
        return False


def peek():
    return STACK[top]


SIZE = 10
STACK = [-1] * SIZE

top = -1

push(3)
# print(top, STACK)
#
# push(4)
# print(top, STACK)
#
# push(10)
# print(top, STACK)
#
# print(pop())
# print(top, STACK)
#
# print(pop())
# print(top, STACK)
#
# print(pop())
# print(top, STACK)
#
# print(pop())
# print(top, STACK)

def fibo(n):
    return fibo(n-1) + fibo(n-2)