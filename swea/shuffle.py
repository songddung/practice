T = int(input())

def solve():
    n = int(input())
    ar = list(map(str, input().split()))
    result = []
    if n % 2 == 0:
        half = n // 2

        for i in range(half):
            result.append(ar[i])
            result.append(ar[i+half])
    else :
        half = n // 2

        for i in range(half+1):
            result.append(ar[i])
            if i+half+1 < len(ar) :
                result.append(ar[i+half+1])

    return result
for t in range(1,T+1):
    print(f'#{t}', *solve(), sep=' ')