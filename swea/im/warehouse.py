n = int(input())

ar = [list(map(int, input().split())) for _ in range(n)]
mx = 0
idx = 0

for i in ar:
    if mx < i[1]:
        mx = i[1]
    if idx < i[0]:
        idx = i[0]
arr = [0]*(idx+1)
for i in ar:
    arr[i[0]] = i[1]

idx = arr.index(mx)

mx = 0
t= 0
for i in range(idx+1):
    if arr[i] > mx :
        mx = arr[i]
    t += mx

mx = 0
for i in range(len(arr)-1, idx,-1):
    if arr[i] > mx:
        mx = arr[i]
    t+= mx
print(t)