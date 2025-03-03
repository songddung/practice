# 직사각형을 만드는 방법

N = int(input())

# 전체 확인
# count = 0
# for i in range(1, N+1):
#     for j in range(i, N+1):
#         if i*j <= N:
#             count += 1
#         if i*j > N:
#             break
# print(count)


# 규칙성 > 몫 연산을 통해
count = N
for i in range(2, N):
    n = N//i - (i-1)
    if n < 1:
        break
    count+= n
print(count)