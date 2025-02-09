### 9X9 표
### 1~9 숫자
### 가로, 세로, 3x3칸에 겹치는 숫자가 있는지 확인 없으면 0 있으면 있으면 1출력


T = int(input())
def sudoku():
    arr = [list(map(int, input().split())) for _ in range(9)]
    count = 1
    for i in range(0, 9, 3):
        # print(i
        for j in range(0, 9, 3):
            # print(f'행 확인')
            ar = arr[i]
            # print(f'1 : {ar}')
            set_ar = set(ar)
            if len(set_ar) < 9:
                # print('행에서 걸림')
                return 0
            else :
                ar = []
                for k in range(3):
                    for h in range(9):
                        # if i + h < 9:
                        ar.append(arr[h][j+k])
                    # print(f'{k}열 확인')
                    # print(f'2 : {ar}')
                    set_ar = set(ar)
                    if len(set_ar) < 9:
                        # print('열에서 걸림')
                        return 0
                    ar = []
                for l in range(3):
                    for o in range(3):

                        ar.append(arr[l][o])

                # print(f'스도쿠 확인')
                # print(ar)
                set_ar = set(ar)
                if len(set_ar) < 9:
                    # print('스도쿠에서 걸림')
                    return 0
    return count
for t in range(1, T + 1):
    # print(f'{t}번쨰')
    print(f'#{t} {sudoku()}')
