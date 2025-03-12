# # 재귀
# def KFC(num):
#     if num == 3:
#         return
#
#     # 재귀 호출 전 들어가야 할 로직
#     print(num, end=' ')
#     KFC(num + 1)
#     KFC(num + 1)
#
#     # 돌아오면서 해야 할 로직
#     # print(num, end=' ')
#
#
# KFC(0)
# print('끝')

# 순열
# [0, 1, 2] 3개의 카드 존재
# 2개를 뽑을 예정

# path = []
#
#
# def recur(count):
#     if count == 2:
#         print(*path)
#         return
#
#     ar = [1, 3, 4, 5, 7]
#     used = [0] * (max(ar)+1)  # 숫자 사용 여부 확인
#     # 조금 더 어려운 문제의 경우
#     # 리스트 방식은 메모리 초과 가능성 존재
#     # dictionary or set 사용 => O(1)
#
#
#     for num in ar:
#         # if num not in path:  # in: 배열의 모든항목 검사 > 시간 오래걸림
#         if used[num] == 0:
#             used[num] = 1
#             path.append(num)
#             recur(count+1)
#             path.pop()
#             used[num] = 0
#
# # 제일 처음 호출할 때 시점이므로
# # 초기값을 전달하면서 시작
# recur(0)

