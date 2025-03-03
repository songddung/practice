# 도로와 신호등

# N : 신호등 갯수, L : 도로의 길이
# D,R,G : 신호등위치, 빨간불 시간, 초록불 시간

N, L = map(int,input().split())
ar = [list(map(int, input().split())) for _ in range(N)]

time = 0 # 누적 시간
i = 0
n = 0
while i < L:
    i += 1
    time += 1
    if n < N :
        if ar[n][0] == i:
            cicle = ar[n][1] + ar[n][2]
            if time % cicle < ar[n][1]:
                time +=  ar[n][1] -time % cicle
            n += 1

print(time)