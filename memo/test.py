arr = []
select = []
select_num = []
L = int(input())
for i in range(L) :
    arr.append(0)
N = int(input())


for i in range(1, N+1) :
    
    select = list(map(int, input().split()))
  
    if i == 1 :
        for j in range(select[0],select[1]+1):
            arr[j-1] = i
    else :
        for k in range(select[0], select[1]+1) :
            if arr[k-1] == 0 :
                print(f'k:{k}')
                arr[k-1] = i
                print(arr)
            else :
                continue
    select_num.append(select)




index_num = []
for z in range(1, N+1) :
    index_num.append(arr.count(int(z)))
    
print(max(index_num))
