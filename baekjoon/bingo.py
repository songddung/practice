# arr = []
# arr2 = []
#
# for i in range(5):
#     arr.append(list(map(int,input().split())))
# for j in range(5):
#     arr2.append(list(map(int,input().split())))
#
# bingo = 0
# my_dict = {}
#
# index = 0
# while index < 25:
#     number = arr2[index//5][index%5]
#     my_dict[number] = True
#
#
#     for e in range(5):
#         for r in range(5):
#             if arr[e][r] == number:
#                 arr[e][r] = 0
#
#     for i in range(5):
#         zero = True
#         for j in range(5):
#             if arr[i][j] != 0:
#                 zero = False
#                 break
#         if zero:
#             bingo +=1
#
#     for j in range(5):
#         zero = True
#         for i in range(5):
#             if arr[i][j] != 0:
#                 zero = False
#                 break
#         if zero:
#             bingo +=1
#
#     zero = True
#     for i in range(5):
#         if arr[i][i] != 0:
#             zero = False
#             break
#     if zero:
#         bingo += 1
#     for i in range(5):
#         if arr[i][4-i] != 0:
#             zero = False
#             break
#     if zero:
#         bingo +=1
#     if bingo >=3:
#         print(index+1)
#         exit()
#     index += 1
arr = []
arr2 = []

# 빙고판 입력
for i in range(5):
    arr.append(list(map(int, input().split())))

# 불러주는 숫자 입력
for j in range(5):
    arr2.append(list(map(int, input().split())))

bingo = 0
index = 0

# 빙고판의 상태를 추적하기 위한 리스트
row_check = [0] * 5
col_check = [0] * 5
diag1_check = 0
diag2_check = 0

while index < 25:
    number = arr2[index // 5][index % 5]

    # 해당 숫자를 빙고판에서 0으로 변경
    for e in range(5):
        for r in range(5):
            if arr[e][r] == number:
                arr[e][r] = 0
                row_check[e] += 1
                col_check[r] += 1
                if e == r:
                    diag1_check += 1
                if e + r == 4:
                    diag2_check += 1

    # 가로 체크
    for i in range(5):
        if row_check[i] == 5:
            bingo += 1

    # 세로 체크
    for j in range(5):
        if col_check[j] == 5:
            bingo += 1

    # 대각선 체크
    if diag1_check == 5:
        bingo += 1
    if diag2_check == 5:
        bingo += 1

    # 빙고가 3개가 되면 결과 출력
    if bingo >= 3:
        print(index + 1)  # index는 0부터 시작하므로 +1
        break  # 루프 종료

    index += 1
