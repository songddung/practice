# 도로와 신호등

# N : 신호등 갯수, L : 도로의 길이
# D,R,G : 신호등위치, 빨간불 시간, 초록불 시간

N, L = map(int,input().split())
ar = [list(map(int, input().split())) for _ in range(N)]

time = 0 # 누적 시간
i = 0 # 이동거리
n = 0 # 신호등 위치

while i < L: # 이동거리가 도로의 길이보다 짧을때 반복
    i += 1 # 이동 거리 추가
    time += 1 # 시간 추가
    if n < N : # 현재 신호등이 주어진 신호등 갯수보다 적을떄
        if ar[n][0] == i: # 현재 위치가 신호등이라면
            cicle = ar[n][1] + ar[n][2] # 신호등 사이클 : 빨간불 + 초록불
            if time % cicle < ar[n][1]: # 시간을 사이클로 나눈뒤 나머지가 빨간불 보다 작다면
                time += ar[n][1] - time % cicle # 대기시간 : 빨간불 - 누적시간%신호등 사이클 추가
            n += 1 # 신호등 번호 변경

print(time)
































