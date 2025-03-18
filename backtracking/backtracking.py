# # N-Queen
# # - y,x 좌표에 queen을 놓은적이 있는지 기록
# #   visited 기록
# #   - 1. 이차원 배열
# #   - 2. 일차원 배열로 효율적으로 하는 방법
#
# # level : N개의 행에 모두 놓으면, 성공
# # branch : N개의 열


def check(y, x):
    # 세로줄, 주 대각선, 부 대각선에 퀸이 이미 있는지 한 번의 for문으로 확인
    for i in range(y):
        if visited[i][x]:  # 세로줄 체크
            return False
        if x - (y - i) >= 0 and visited[i][x - (y - i)]:  # 주 대각선 체크
            return False
        if x + (y - i) < N and visited[i][x + (y - i)]:  # 부 대각선 체크
            return False
    return True


def dfs(row):
    global result
    if row == N:
        result += 1
        return

    # 후보군 : N 개의 열에 대해서
    for col in range(N):
        if not check(row, col):
            continue
        visited[row][col] = 1
        dfs(row+1)
        visited[row][col] = 0


N = 8
visited = [[0] * N for _ in range(N)]
result = 0

dfs(0)
print(result)
