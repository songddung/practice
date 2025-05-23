# ### 버블 정렬
# N = 5
# numbers = [55, 7, 78, 12, 42]
#
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# print(numbers)
#
#
# ### 카운팅 정렬
# arr = [0, 4, 1, 3, 1, 2, 4, 1]
#
# num = 0
# for j in arr:
#     if num < j:
#         num = j
# ar = [0] * (num + 1)
#
#
# for i in arr:
#     ar[i] += 1
# print(ar)
#
#
# for i in range(1, len(ar)):
#     ar[i] += ar[i-1]
# print(ar)
#
# temp = [0] * len(arr)
# print(temp)
# for i in range(len(arr)-1, -1, -1):
#     ar[arr[i]] -= 1
#     temp[ar[arr[i]]] = arr[i]
# print(temp)
#
# ### 완전검색
# arr = [2, 3, 7]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i != j:
#             for k in range(len(arr)):
#                 if k != i and k != j:
#                     print(arr[i], arr[j], arr[k])
#
#
# ### 탐욕 알고리즘
# num = 456789
# c = [0] * 12
#
# for i in range(6):
#     c[num % 10] += 1
#     num //= 10
# print(c)
#
# i = 0
# tri = 0
# run = 0
#
# while i < 10:
#     if c[i] >= 3:
#         c[i] -= 3
#         tri += 1
#         continue
#     if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
#         c[i] -= 1
#         c[i+1] -= 1
#         c[i+2] -= 1
#         run += 1
#         continue
#     i += 1
# if run + tri == 2: print("Baby Gin")
# else: print("Lose")

# print(1 - (-1))

arr = []
arr2 = []

# 빙고판 입력
i = 0
while i < 5:
    arr.append(list(map(int, input().split())))
    i += 1

# 사회자가 부르는 수 입력
j = 0
while j < 5:
    arr2.append(list(map(int, input().split())))
    j += 1

# 빙고 체크를 위한 변수
bingo_count = 0
called_numbers = {}

# 사회자가 부르는 수를 순서대로 처리
call_index = 0
while call_index < 25:
    number = arr2[call_index // 5][call_index % 5]
    called_numbers[number] = True

    # 빙고판에서 해당 숫자를 0으로 변경
    for i in range(5):
        for j in range(5):
            if arr[i][j] == number:
                arr[i][j] = 0

    # 빙고 체크
    # 가로 체크
    for i in range(5):
        all_zero = True
        for j in range(5):
            if arr[i][j] != 0:
                all_zero = False
                break
        if all_zero:
            bingo_count += 1

    # 세로 체크
    for j in range(5):
        all_zero = True
        for i in range(5):
            if arr[i][j] != 0:
                all_zero = False
                break
        if all_zero:
            bingo_count += 1

    # 대각선 체크
    all_zero = True
    for i in range(5):
        if arr[i][i] != 0:
            all_zero = False
            break
    if all_zero:
        bingo_count += 1

    all_zero = True
    for i in range(5):
        if arr[i][4 - i] != 0:
            all_zero = False
            break
    if all_zero:
        bingo_count += 1

    # 빙고가 3개가 되면 결과 출력
    if bingo_count >= 3:
        print(call_index + 1)  # 몇 번째 수를 부른 후
        exit()

    call_index += 1
