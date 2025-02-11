T = int(input())
def solve():
    a,b,n = map(int,input().split())
    count = 0

    while (a <= n) and (b <= n):
        if a < b:
            a += b
            count += 1
        else :
            b += a
            count += 1

    return count
for t in range(T):

    print(solve())


#