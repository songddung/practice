n, m = map(int, input().split())
second_line = list(map(int, input().split()))
arr = []
arr2 = []
second_line.sort()

for i in range(n) :
    for j in range(n-1) :
        for k in range(n-2) :
            arr.append(second_line[i]+second_line[j+1]+second_line[k+2])

for i in range(len(arr)) :
     arr2.append(m - arr[i])
     print(arr2)

arr2.sort()

for i in range(len(arr2)) :
    if 0 == arr2[i] :
        print(m)
        break
    if arr2[i] > 0 :
        print(m+arr2[i])
        break
 