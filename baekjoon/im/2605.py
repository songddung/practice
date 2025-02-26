n = int(input())
ar = list(map(int, input().split()))
arr = []

for i in range(1, n+1):
    arr.insert(ar[i-1],i)

print(*arr[::-1])