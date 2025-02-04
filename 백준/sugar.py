### 설탕배달(2839)
# input = 총무게
# 출력 : 봉지 갯수
# 정수로 떨어지지 않을 경우 -1 출력

### 1번 (fail)
# 5로 먼저나누고 나머지를 3으로 나누기

### 2번 
# 

N = int(input())
ar=[]
check = 0
for i in range((N//5)+1):
    a = N - (5*i)
    if a % 3 == 0 :
        ar.append([i, a//3])
        check = 1

if check == 0 :
    print(-1)
    exit()
else :
    mn = sum(ar[0])
    for j in ar :
        if sum(j) < mn :
            mn = sum(j)


print(mn)