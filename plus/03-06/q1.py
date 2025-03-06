N, M = map(int, input().split())
ar = list(map(int, input().split()))
for i in range(M):
    st, ed = map(int, input().split())
    print(sum(ar[st-1:ed]))