T = int(input())

def solve():
    n = int(input())
    ar = [[] for _ in range(n)]
    idx = 0
    col = 0

    for i in range(n):
        txt , num = map(str, input().split())
        num = int(num)
        for k in range(num):
            if col == 10:
                idx += 1
                col = 0
            ar[idx].append(txt)
            col += 1
    return ar


for t in range(1, T+1):
    result = solve()
    print(f'#{t}')
    for arr in result:
        print(*arr, sep='')