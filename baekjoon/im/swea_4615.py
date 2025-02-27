T = int(input())


def solve():
    N, M = map(int,input().split())
    ar = [[0] * N for _ in range(N)]
    ar[N//2-1][N//2-1] = 2  # 돌색 잘보고 넣자 이거 바꿔넣어서 3번 틀림
    ar[N//2-1][N//2] = 1
    ar[N//2][N//2-1] = 1
    ar[N//2][N//2] = 2
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]  # 상하좌우 + 대각선4방향

    for i in range(M):
        col, row, color = map(int, input().split())
        row -= 1
        col -= 1
        ar[row][col] = color

        for k in range(8):
            stack = []  # 방향 탐색 중 나랑 다른 색 돌이면 좌표 저장할 리스트
            dy, dx = row + direct[k][0], col + direct[k][1]
            while 0 <= dy < N and 0 <= dx < N:  # 일단 출발
                if ar[dy][dx] == 0:  # 0이면 반복문 종료
                    break
                if ar[dy][dx] == color:  # 나랑 같은 색 돌만나면 스택에 있는 좌표 뺴서 나랑 같은 색으로 돌바꾸기
                    for py, px in stack:
                        ar[py][px] = color
                    break  # 다 바꿨으면 종료
                stack.append((dy, dx))  # if문을 안타면 다른 색 돌이니까 스택에 좌표 저장
                dy += direct[k][0]  # 방향탐색 거리 추가
                dx += direct[k][1]


    black_count = 0
    white_count = 0
    for i in range(N):  # 돌 세기
        black_count += ar[i].count(1)
        white_count += ar[i].count(2)
    return black_count, white_count




for t in range(1, T+1):
    print(f'#{t}', *solve())