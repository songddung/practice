### 수열 (2559)
# input1 = 날짜, 수열
# input2 날짜별 온도

### 슬라이딩 윈도우
# [0:4] > [1:5] > [2:6] 와 같이 첫부분과 끝부분만 변경
 


# 입력 받기
input1 = list(map(int, input().split()))
input2 = list(map(int, input().split()))

N = input1[0]  # 전체 날짜 수
K = input1[1]  # 연속적인 날짜 수

# 초기 K일의 온도 합 계산
current_sum = sum(input2[:K]) # 인덱스 0 ~ 4를 모두 합치기
max_sum = current_sum 

# 슬라이딩 윈도우를 사용하여 최대 합 계산
for i in range(K, N): # 수열 ~ 전체날짜   ex) 5 ~ 10
    current_sum += input2[i] - input2[i - K]  # 새로운 날 추가하고, 가장 오래된 날 제거
    if current_sum > max_sum: # 새로운 합이 기존합보다 클 경우 변경
        max_sum = current_sum

print(max_sum)

