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
# 많이 받은 사람
# select_num 리스트에 각 번호를 세서
# 가장 많은사람 동점이 있을 경우 인덱스가 낮은 사람
index1 = 0
for z in range(1, N+1) :

    pass

# 많이 받을줄 알았던 사람
# select_num 리스트에 하나씩 뽑아서 뒷번호에서 앞번호를 빼고 가장 큰사람
# 동점이 있을 경우 인덱스가 낮은 사람
prediction = []
index2 = 0
for i in range(N) :
    pass