# 치즈
# N, M = 행, 열
# 치즈가 존재하면 1로 표기하여 리스트 받음
# 0과 닿아있는 부분은 c로 변경 -> 반복문 안에 넣기
# c제거 후 time += 1
# 출력 : 전부 녹는데 걸리는 시간, 다녹기 한시간전 치즈조각 수
from collections import deque

N, M = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]


direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time = 0



def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1


    # 공기접촉 여부 확인 후 c덱에 넣기
    while q:
        ci, cj = q.popleft()

        for dy, dx in direct:
            ni, nj = ci + dy, cj + dx

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 :
                visited[ni][nj] = 1
                if ar[ni][nj] == 0:
                    q.append((ni, nj))
                elif ar[ni][nj] == 1:
                    c.append((ni, nj))



while True:
    c = deque()
    total = sum(row.count(1) for row in ar)


    if total == 0:
        break
    else:
        check = total


    bfs()

    while c:
        dy, dx = c.popleft()
        ar[dy][dx] = 0
    time += 1


print(time)
print(check)