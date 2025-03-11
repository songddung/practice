T = int(input())


def calc(k, mid_sum):

    global mx, mn
    if k == N-1:

        if mid_sum > mx:
            mx = mid_sum
        if mid_sum < mn:
            mn = mid_sum

    if operator[0] > 0:
        operator[0] -= 1
        calc(k+1, mid_sum + ar[k+1])
        operator[0] += 1

    if operator[1] > 0:
        operator[1] -= 1
        calc(k+1, mid_sum - ar[k+1])
        operator[1] += 1

    if operator[2] > 0:
        operator[2] -= 1
        calc(k+1, mid_sum * ar[k+1])
        operator[2] += 1

    if operator[3] > 0:
        operator[3] -= 1
        calc(k+1, int(mid_sum / ar[k+1]))
        operator[3] += 1


def solve():
    global N, operator, ar, mx, mn
    N = int(input())
    mx = -10 ** 8
    mn = 10 ** 8

    operator = list(map(int, input().split()))
    ar = list(map(int, input().split()))


    calc(0, ar[0])
    return mx - mn


for t in range(1, T+1):
    print(f'#{t} {solve()}')

'''
1
5
2 1 0 1
3 5 3 7 9
'''
#
# def calc(k, mid_sum, N, operator, ar, mx, mn):
#     if k == N - 1:
#         if mid_sum > mx:
#             mx = mid_sum
#         if mid_sum < mn:
#             mn = mid_sum
#         return mx, mn
#
#     # Try each operator
#     if operator[0] > 0:  # Addition
#         operator[0] -= 1
#         mx, mn = calc(k + 1, mid_sum + ar[k + 1], N, operator, ar, mx, mn)
#         operator[0] += 1
#
#     if operator[1] > 0:  # Subtraction
#         operator[1] -= 1
#         mx, mn = calc(k + 1, mid_sum - ar[k + 1], N, operator, ar, mx, mn)
#         operator[1] += 1
#
#     if operator[2] > 0:  # Multiplication
#         operator[2] -= 1
#         mx, mn = calc(k + 1, mid_sum * ar[k + 1], N, operator, ar, mx, mn)
#         operator[2] += 1
#
#     if operator[3] > 0:  # Division
#         operator[3] -= 1
#         mx, mn = calc(k + 1, int(mid_sum / ar[k + 1]), N, operator, ar, mx, mn)  # Use integer division
#         operator[3] += 1
#
#     return mx, mn
#
# def solve():
#     N = int(input())  # Number of elements
#     mx = -10**8  # Initial maximum value
#     mn = 10**8   # Initial minimum value
#
#     operator = list(map(int, input().split()))  # Operators count: [+, -, *, //]
#     ar = list(map(int, input().split()))  # The array of numbers
#
#     mx, mn = calc(0, ar[0], N, operator, ar, mx, mn)  # Start recursion with the first number in ar[0]
#     return mn, mx
#
# T = int(input())  # Number of test cases
# for t in range(1, T + 1):
#     mn, mx = solve()
#     print(f'#{t} {mn} {mx}')
