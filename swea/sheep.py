

T = int(input())

def solve():
    n = int(input())
    ar = []
    count = 0
    x = 1

    while len(ar) < 10:
        nx = n * x
        count += 1
        x += 1
        for i in str(nx):
            if i not in ar:
                ar.append(i)
    return count*n


for t in range(1, T+1):
    print(f'#{t} {solve()}')