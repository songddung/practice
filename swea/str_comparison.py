T = int(input())

def solve():
    n = input()
    m = input()

    len_n = len(n)
    len_m = len(m)
    for i in range(len_m-len_n+1):
        check = m[i:i+len_n]
        if n == check:
            return 1
    return 0

for t in range(1,T+1):
    print(f'#{t} {solve()}')