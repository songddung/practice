N = int(input())

ar = list(map(int, input().split()))
M = max(ar)

counting = [0]*(M+1)

for i in ar:
    counting[i] += 1

for i in range(1, len(counting)):

    print(f'{i} {counting[i]}')









