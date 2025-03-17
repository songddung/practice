# SWEA 병합정렬

T = int(input())


def solve(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = solve(lst[:mid])
    right = solve(lst[mid:])
    return merge(left, right)


def merge(left, right):
    global result
    arr = []
    i = j = 0

    if left[-1] > right[-1]:
        result += 1
    while i < len(left) and j < len(right):
        if left[i] > right[j]:

            arr.append(right[j])
            j += 1
        else:
            arr.append(left[i])
            i += 1
    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr


for t in range(1, T+1):
    result = 0
    N = int(input())
    ar = list(map(int, input().split()))
    sort_ar = solve(ar)
    print(f'#{t} {sort_ar[N//2]} {result}')

