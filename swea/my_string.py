T = 10

def solve():
    t = int(input())
    p = input()
    txt = input()
    i = 0
    count = 0

    while i <= len(txt) - len(p):
        if txt[i:i+len(p)] == p:
            count += 1
            i += len(p)
        else:
            i += 1

    print(f'#{t} {count}')
for _ in range(1, T+1):
    solve()

