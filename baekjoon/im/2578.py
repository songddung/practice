# 빙고

ar = [list(map(int, input().split())) for _ in range(5)]

check = []
for i in range(5):
    check.extend(map(int, input().split()))  # extend() : 다른 배열의 요소를 추가, 1차원으로 데이터 받기위해 사용함

def solve():
    for k in range(25):
        # 현재 부른 숫자에 대해 빙고판에서 체크
        for i in range(5):
            for j in range(5):
                if ar[i][j] == check[k]:
                    ar[i][j] = 0  # 해당 숫자를 0으로 변경

                    # 빙고 카운트 초기화
                    bingo = 0

                    # 가로 체크
                    for row in ar:
                        if row.count(0) == 5:
                            bingo += 1

                    # 세로 체크
                    for j in range(5):
                        count = 0
                        for i in range(5):
                            if ar[i][j] == 0:
                                count += 1
                        if count == 5:
                            bingo += 1

                    # 대각선 체크 (왼쪽 위 -> 오른쪽 아래)
                    count = 0
                    for i in range(5):
                        if ar[i][i] == 0:
                            count += 1
                    if count == 5:
                        bingo += 1

                    # 대각선 체크 (오른쪽 위 -> 왼쪽 아래)
                    count = 0
                    for i in range(5):
                        if ar[i][4 - i] == 0:
                            count += 1
                    if count == 5:
                        bingo += 1

                    # 3개의 빙고가 완성되면 출력
                    if bingo >= 3:
                        return k + 1

print(solve())
