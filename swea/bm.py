T = int(input())

def solve():
    p = input()
    t = input()

    count = 0
    for i in range(len(t)-len(p)+1):
        if t[i] == p[0]:
            for j in range(len(p)):
                if t[i+j] != p[j]:
                    break
            else:
                count += 1
            if count == 1:
                return 1
    return 0

for k in range(1,T+1):
    print(f'#{k} {solve()}')