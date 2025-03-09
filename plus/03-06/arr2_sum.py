N, M = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    total += sum(ar[i])
print(total)