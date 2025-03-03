# 나이트의 이동
# input1 : 테스트케이스 개수
    # 3줄씩 input 받음
    # input1 : 체스판 길이 (정사각형)
    # input2 : 현재 나이트 좌표
    # input3 : 목표 좌표
# 나이트의 이동 : 한칸 대각선

def bfs():
    q = []
    q.append((si, sj))

    while q:
        ci, cj = q.pop(0)
        if ci == ei and cj == ej:
            return visited[ci][cj] - 1 # 시작위치를 1로 시작해서 이동횟수는 -1해줘야 함

        for k in range(8):
            dy, dx = ci + direct[k][0], cj + direct[k][1]
            if 0 <= dy < N and 0 <= dx < N and visited[dy][dx] == 0:
                # visited 를 단순히 방문여부를 파악하는 1로만 넣지않고 이전좌표의 값 + 1로 넣어 이동 횟수를 파악
                visited[dy][dx] = visited[ci][cj] + 1
                q.append((dy, dx))



T = int(input())
direct = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)] # 나이트의 이동 한칸 대각선

for t in range(T):
    N = int(input())
    visited = [[0]*N for _ in range(N)]

    sj, si = map(int, input().split())
    visited[si][sj] = 1 # 시작 위치로 되돌아 오지 않도록 방문 표시
    ej, ei = map(int, input().split())
    print(bfs())
    for i in range(N):
        print(visited[i])
