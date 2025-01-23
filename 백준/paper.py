### 10, 10 정사각형 색종이
# 100, 100 도화지
# 1라인 색종이수

### 2~라인
# 1번 : 색종이 왼쪽변과 도화지 왼쪽 변 간격
# 2번 : 색종이 아래쪽 변과 도화지 아래쪽 변 간격




input1 = int(input())
input2 = []
for i in range(input1) :
    input2.append(list(map(int,input().split())))

sum_number = input1 * 100 # 총 색종이 넓이 합

for i in range(len(input2)-1) :
    for j in  range(1,len(input2)) :
        if i == j :
            continue

        if abs(input2[i][0] - input2[j][0]) < 10 :
            x = 10 - abs(input2[i][0] - input2[j][0])  
            y = 10 - abs(input2[i][1] - input2[j][1])
            minus = x * y
            sum_number -= minus
print(sum_number)