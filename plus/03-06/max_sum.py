N, K = map(int, input().split())
ar = list(map(int, input().split()))

mx = sum(ar[:K])
num = mx
for i in range(K, N):
    num = num - ar[i-K] + ar[i]
    mx = max(mx, num)

print(mx)