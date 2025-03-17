# 퀵 정렬
T = int(input())


def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = len(lst)//2
    left = [x for x in lst if x < lst[pivot]]
    middle = [x for x in lst if x == lst[pivot]]
    right = [x for x in lst if x > lst[pivot]]
    return quick_sort(left) + middle + quick_sort(right)


for t in range(1, T+1):
    N = int(input())
    ar = list(map(int, input().split()))
    srt_ar = quick_sort(ar)
    print(f'#{t} {srt_ar[N//2]}')

#
#
#
#
# import random
# T = int(input())
#
# def insertion_sort(arr, left, right):
#     for i in range(left + 1, right + 1):
#         key = arr[i]
#         j = i - 1
#         while j >= left and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
# def quick_sort(arr, left, right):
#     # 배열이 작을 경우 삽입 정렬로 전환
#     if right - left <= 10:
#         insertion_sort(arr, left, right)
#         return
#
#     # 피벗을 랜덤으로 선택
#     pivot_index = random.randint(left, right)
#     pivot = arr[pivot_index]
#     arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # 피벗을 끝으로 보냄
#
#     i = left - 1
#     for j in range(left, right):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[right] = arr[right], arr[i + 1]
#     pivot_index = i + 1
#
#     # 피벗을 기준으로 왼쪽과 오른쪽을 분할하여 재귀적으로 정렬
#     quick_sort(arr, left, pivot_index - 1)
#     quick_sort(arr, pivot_index + 1, right)
#
#
# # 예시 실행
# for t in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     quick_sort(arr, 0, len(arr) - 1)
#     print(f'#{t} {arr[N//2]}')
