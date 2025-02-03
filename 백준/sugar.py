### 설탕배달(2839)
# input = 총무게
# 출력 : 봉지 갯수
# 정수로 떨어지지 않을 경우 -1 출력

### 1번 (fail)
# 5로 먼저나누고 나머지를 3으로 나누기

### 2번 
# 




# if N < 5 :
#     three_remain = N % 3
#     if three_remain == 0 :
#         bag = N // 3
#     else :
#         bag = -1
# else :
#     while True :
#         five = N // 5
#         five_remain = N % 5

#         if five_remain == 0 :
#             bag = five
#         else :
            
#             for i in range(1, five+1):
#                 # N - (5 * (i-1)) // 3
#                 ii = (N - ((five-i)*5)) % 3
#                 if ii % 3 == 0 :
#                     five_i = five - i 
#                     three_i = (N - (five_i*5)) // 3
#                     bag = five_i+three_i
#                     print(bag)
#                     break
#             break

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