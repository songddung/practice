N = int(input())
ar = list(map(int, input().split()))

mx = 0
mn = ar[0]

for i in ar:
    mx = i if mx < i else mx
    mn = i if mn > i else mn
print(mx, mn)