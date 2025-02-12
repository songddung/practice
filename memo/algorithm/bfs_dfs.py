# 다이렉트 배열 상하좌우
direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve():
    n = int(input())
    ar = [list(map(int, input().split())) for _ in range(n)]

    # 배열 원소 순회
    for i in range(n):
        for j in range(n):
            # 중앙값을 먼저 더함
            t = ar[i][j]

            # 다이렉트 배열 크기만큼 = 상하좌우를
            for k in range(4):
                # 새로운 좌표 dy(i), dx(j) 생성해서
                dy, dx = i + direct[k][0], j + direct[k][1]

                # 만약 새로운 좌표가 인덱스 안벗어난다면
                if 0 <= dy < n and 0 <= dx < n:
                    # t에 거기 원소 더함
                    t += ar[dy][dx]

###################################################################################################################
# 다이렉트 배열 상하좌우
direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve():
    n = int(input())
    ar = [list(map(int, input().split())) for _ in range(n)]

    # 배열 원소 순회
    for i in range(n):
        for j in range(n):
            # 중앙값을 먼저 더함
            t = ar[i][j]

            # 다이렉트 배열 크기만큼 = 상하좌우를
            for k in range(4):
                # 범위만큼 (여기선 전체인덱스범위만큼 = 크아 물풍선)
                for l in range(1, n):
                    # 새로운 좌표 dy(i) * 범위, dx(j) * 범위 생성해서
                    dy, dx = i + direct[k][0] * l, j + direct[k][1] * l

                    # 만약 새로운 좌표가 인덱스 안벗어난다면
                    if 0 <= dy < n and 0 <= dx < n:
                        # t에 거기 원소 더함
                        t += ar[dy][dx]