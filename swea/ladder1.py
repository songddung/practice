### 맨 아랫줄에서 2찾아서 스타트
### 좌우먼저 확인 1이면 해당 방향 0나올때 까지 이동
### 좌우가 0이면 위로 이동
# row_idx == 0이면 끝
T = 10

def solve():
    n = int(input())
    ar = [list(map(int, input().split())) for _ in range(100)]
    l, r = -1, 1

    row_idx = 99
    col_idx = 0
    for i in range(100): ## 2의 위치 찾기
        if ar[row_idx][i] == 2:
            col_idx = i
            break
    row_idx -= 1

    while row_idx > -1: # row 0까지
        while col_idx+l >= 0 and ar[row_idx][col_idx+l] == 1: # 왼쪽확인
            # print('좌측  while')
            ar[row_idx][col_idx] = 0
            col_idx += l # 1이면 이동

        while col_idx+r <= 99 and ar[row_idx][col_idx+r] == 1: # 오른쪽 확인
            # print('우측  while')
            ar[row_idx][col_idx] = 0
            col_idx += r
        row_idx -= 1
    return col_idx

for t in range(1, T+1):
    print(f'#{t} {solve()}')



