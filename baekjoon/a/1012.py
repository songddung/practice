# 유기농 배추
# input1 : 테스트케이스 수
# input2 : 가로길이, 세로길이, 배추가 심겨져있는 위치의 갯수
# 붙어있는 배추의 필드 갯수 반환
# 방향탐색으로 visited 변환
# 방문하지 않았던 좌표라면 count += 1



def bfs(si, sj):
    q = []
    q.append((si, sj))

    while q:
        ci, cj = q.pop()
        for k in range(4):
            dy, dx = ci + direct[k][0], cj + direct[k][1]

            if 0 <= dy < row and 0 <= dx < col and visited[dy][dx] == 0 and ar[dy][dx] == 1:
                q.append((dy,dx))
                visited[dy][dx] = 1



T = int(input())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for t in range(T):
    col, row, num = map(int, input().split())
    visited = [[0]*col for _ in range(row)]  # visited 선언 시 1차원인지 2차원인지 보고 선언
    result = 0
    ar = [[0]*col for _ in range(row)]

    for _ in range(num):
        c,r = map(int, input().split())
        ar[r][c] = 1

    for i in range(row):
        for j in range(col):
            if ar[i][j] == 1 and visited[i][j] == 0:
                result += 1
                bfs(i,j)

    print(result)