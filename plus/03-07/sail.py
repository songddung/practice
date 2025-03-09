T = int(input())


def solve():
    N = int(input())
    ar = list(map(int, input().split()))
    ar.reverse()
    result = []

    while ar:
        num = ar[0]
        check = int(num * 0.75)
        if check in ar:
            ar.remove(num)
            ar.remove(check)
            result.append(check)
    result.reverse()
    return result

for t in range(1, T+1):
    print(f'#{t}' , *solve())

'''
2
3
15 20 60 75 80 100
4
90 90 120 120 120 150 160 200
'''