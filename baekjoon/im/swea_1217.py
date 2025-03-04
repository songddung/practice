# 거듭제곱
# 재귀호출로 풀기


T = 10

def power(n1, n2):
    if n2 == 0:
        return 1


    return n1 * power(n1, n2-1)
def solve():
    tc = int(input())
    num1, num2 = map(int, input().split())
    return tc,power(num1, num2)


for t in range(1, T+1):
    tc, v = solve()
    print(f'#{tc} {v}')