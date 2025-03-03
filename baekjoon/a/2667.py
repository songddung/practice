# 단지번호 붙이기
# 상하좌우에 연결되어있으면 카운트 하나씩 증가
# 방문한곳은 카운트 증가 x
# visited 전역으로 선언
# 정사각형 배열

# bfs: 시작위치 받아서 해당 위치에 연결된 1의 개수를 리턴
def bfs(si, sj):
    q = [] # 큐등 필요 변수 생성

    q.append((si, sj)) # 큐에 초기 데이터 삽입
    visited[si][sj] = 1 # 방문 표시
    count = 1 # 정답처리 관련 작업

    while q: # 큐에 좌표가 들어있으면
        cy, cx = q.pop()  # 큐에서 좌표 추출
        for k in range(4): #  4방향 방향탐색
            dy, dx = cy + direct[k][0], cx + direct[k][1] #
            if 0 <= dy < N and 0 <= dx < N and visited[dy][dx] == 0 and ar[dy][dx] == 1: # 범위내, 방문x, 1이면
                q.append((dy,dx)) # 큐에 넣기
                visited[dy][dx] = 1 # 방문표시
                count +=1 # 카운트 증가
    return count# 단지번호 붙이기
# 상하좌우에 연결되어있으면 카운트 하나씩 증가
# 방문한곳은 카운트 증가 x
# visited 전역으로 선언
# 정사각형 배열

# bfs: 시작위치 받아서 해당 위치에 연결된 1의 개수를 리턴
def bfs(si, sj):
    q = [] # 큐등 필요 변수 생성

    q.append((si, sj)) # 큐에 초기 데이터 삽입
    visited[si][sj] = 1 # 방문 표시
    count = 1 # 정답처리 관련 작업

    while q: # 큐에 좌표가 들어있으면
        cy, cx = q.pop()  # 큐에서 좌표 추출
        for k in range(4): #  4방향 방향탐색
            dy, dx = cy + direct[k][0], cx + direct[k][1] #
            if 0 <= dy < N and 0 <= dx < N and visited[dy][dx] == 0 and ar[dy][dx] == 1: # 범위내, 방문x, 1이면
                q.append((dy,dx)) # 큐에 넣기
                visited[dy][dx] = 1 # 방문표시
                count +=1 # 카운트 증가
    return count



N = int(input())
ar = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = []

for i in range(N):
    for j in range(N):
        if ar[i][j] == 1 and visited[i][j] == 0: # 1이고 방문하지 않았다면
            result.append(bfs(i,j))

result.sort()
print(len(result), *result, sep='\n')







N = int(input())
ar = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = []

for i in range(N):
    for j in range(N):
        if ar[i][j] == 1 and visited[i][j] == 0: # 1이고 방문하지 않았다면
            result.append(bfs(i,j))

result.sort()
print(len(result), *result, sep='\n')



