n = int(input())
ar = list(map(int, input().split()))
arr = []

for i in range(1, n+1):
    arr.insert(ar[i-1],i)  # insert(i,v) : i : 인덱스, v : 넣고 싶은 값
    print(arr)
print(*arr[::-1])