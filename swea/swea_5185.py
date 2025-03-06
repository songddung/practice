hx = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

T = int(input())


def solve():
    N, st = map(str, input().split())
    N = int(N)
    result = ''
    for i in st:

        num = hx.index(i)


        rs = []
        while num > 0:
            pp = num % 2
            rs.append(str(pp))
            num = num // 2
        while len(rs) < 4:
            rs.append('0')

        rs.reverse()
        for i in rs:
            result += i
    return result

for t in range(1, T+1):
    print(f'#{t} {solve()}')

'''
3
4 47FE
5 79E12
8 41DA16CD
'''