# N, M = map(int, input().split())
# ar = [list(map(int, input().split())) for _ in range(N)]
# mx = 0
#
#
# for i in range(N):
#     for j in range(M):
#         if ar[i][j] == 1:
#
#             for k in range(min(N-i, M-j), 0, -1):
#
#                 check = True
#                 for y in range(i, i+k):
#                     for x in range(j, j+k):
#
#                         if ar[y][x] == 0:
#                             check = False
#                             break
#                     if not check:
#                         break
#                 if check:
#                     mx = max(mx, k)
#                     break
#
#
# print(f'최대 정사각 부분행렬의 크기: {mx}')


N, M = map(int, input().split())  # N, M 입력
ar = [list(map(int, input().split())) for _ in range(N)]  # 행렬 입력
mx = 0  # 가장 큰 정사각형의 크기를 저장할 변수

# DP 배열을 만들어서 각 위치에서 가능한 최대 크기 저장
dp = [[0] * M for _ in range(N)]

# 첫 번째 행과 첫 번째 열 처리 (아래에서 설명)
for i in range(N):
    for j in range(M):
        if ar[i][j] == 1:  # 현재 위치가 1일 때만
            if i == 0 or j == 0:
                dp[i][j] = 1  # 첫 번째 행이나 열에 있는 1은 크기가 1인 정사각형
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1  # 위, 왼쪽, 대각선 중 최소값 + 1

            # 최대값 갱신
            mx = max(mx, dp[i][j])

# 결과 출력
print(f'최대 정사각 부분행렬의 크기: {mx}')
