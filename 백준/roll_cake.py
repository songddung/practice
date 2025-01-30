### 롤케이크 (3985) 
# 길이 L미터 케이크 (1번 input)
# 방청객 N명

arr = [] ### 케이크
select = [] ### 방청객이 선택한 숫자 리스트
select_num = [] ### 숫자 리스트를 넣는 리스트
L = int(input()) # L미터 케이크
for i in range(L) :
    arr.append(0)
N = int(input()) # 방청객 N명


for i in range(1, N+1) :
    
    select = list(map(int, input().split())) # space로 구분하는 리스트 
    select[0] -= 1  # 0-based index로 조정
    select[1] -= 1  # 0-based index로 조정
    ### 방청객에게 처음으로 받은 종이 일 경우
    if i == 1 : 
        ### 받은 숫자에서 숫자까지 번호 넣기
        for j in range(select[0],select[1]+1):
            arr[j] = i
    else :
        ### 처음이 아닐 경우
        for k in range(select[0], select[1]+1) :
            if arr[k] == 0 :
                arr[k] = i
            else :
                continue
    select_num.append(select)


# 많이 받을줄 알았던 사람
# select_num 리스트에 하나씩 뽑아서 뒷번호에서 앞번호를 빼고 가장 큰사람
# 동점이 있을 경우 인덱스가 낮은 사람
prediction = [] # select_num[인덱스][1] - select_num[인덱스][0]
index2 = 0
for i in range(N) :
    prediction.append(select_num[i][1] - select_num[i][0])
max_count = max(prediction)
print(prediction.index(max_count)+1) # 인덱스에서 1더해주기



# 많이 받은 사람
# arr에서 카운트
# 가장 많은사람 동점이 있을 경우 인덱스가 낮은 사람
index1 = 0
max_count = 0
for z in range(1, N+1) :
    count = arr.count(z)
    if count > max_count:
        max_count = count
        index1 = z
print(index1)