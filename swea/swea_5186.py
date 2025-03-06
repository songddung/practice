# 이진수2
T = int(input())


def solve():
    num = float(input())
    i = 1
    result = ''

    while i < 14:
        if num == 0.0:
            return result
        if num - 2**-i >= 0:
            result += '1'
            num -= 2**-i
        else:
            result += '0'
        i += 1
    return 'overflow'

for t in range(1, T+1):
    print(f'#{t} {solve()}')
