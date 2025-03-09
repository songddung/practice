N = int(input())
ar = list(map(int, input().split()))
total = 0

for i in ar:
    total += i

average = total // N

print(total, average)