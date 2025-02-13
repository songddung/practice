T = int(input())

def solve():
    n, c = map(int, input().split())
    ar = list(map(int, input().split()))
    jump = []
    for i in range(c):
        jump.append(list(map(int, input().split())))

    for i in jump:
        which = i[0]-1
        for j in range(1, i[1] + 1):
            if which-j >= 0 and which + j < n:
                if ar[which-j] == ar[which+j]:
                    if ar[which-j] == 1:
                        ar[which-j] = 0
                        ar[which + j] = 0
                    else:
                        ar[which - j] = 1
                        ar[which + j] = 1


    return ar

for t in range(1, T+1):
    print(f'#{t}', end=' ')
    print(*solve(), sep=' ')