N, L = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int,input().split()))) # 거리, 빨간불 시간 , 초록불 시간

time = 0
move = 0
for i in range(N):
    D, R, G = arr[i]


# for i in range(N):
#     D, R, G = arr[i]
#
#     ### 현재 위치에서 신호등까지 이동
#     time += D - move
#     move = D
#
#     # 신호등에서 대기 시간 계산
#     cycle = R + G # 신호등의 전체 사이클 시간
#
#     # 현재 시점에 대한 사이클의 시작지점
#     currunt_time = time % cycle
#
#     ### 빨간불일 경우
#     if currunt_time < R:
#         wait_time = R - currunt_time # 기다려야 할 시간
#         time += wait_time # 총 시간에 대기 시간 추가
# ### 도로 끝까지 이동
# time += L - move
# print(time)