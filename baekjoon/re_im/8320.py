# 직사각형을 만드는 방법

N = int(input())
count = 0

for i in range(1, N+1):
    for j in range(i, N+1):
        if i * j <= N:
            count += 1
        else:
            break
print(count)