def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    global result
    arr = []
    i = j = 0

    if left[-1] > right[-1]:
        result += 1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ar = list(map(int, input().split()))
    result = 0
    sort_ar = merge_sort(ar)

    print(f'#{t} {sort_ar[N//2]} {result}')