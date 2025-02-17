T = int(input())

def solve():
    n, m = map(int, input().split())
    ar = list(map(int, input().split()))
    change = []
    for i in range(m):
        change.append(list(map(int, input().split())))

    for j in change:
        start = j[0]-1
        step = j[1]

        for k in range(1, step+1):
            if start + k < n and start - k >= 0:
                if ar[start + k] == ar[start - k]:
                    if ar[start+k] == 1:
                        ar[start+k] = 0
                        ar[start-k] = 0
                    else:
                        ar[start+k] = 1
                        ar[start-k] = 1
    return ar


for t in range(1, T+1):
    print(f'#{t}', *solve(), sep=' ')


