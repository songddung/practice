T = int(input())

def min_max():
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = arr[0]
    max_num = 0
    min_idx = 0
    max_idx = 0
    for i in range(len(arr)):
        if max_num <= arr[i]:
            max_num = arr[i]
            max_idx = i
        if min_num > arr[i]:
            min_num = arr[i]
            min_idx = i
    result = (max_idx + 1) - (min_idx + 1)
    if result < 0:
        return -(result)
    else:
        return result
for t in range(1, T+1):
    print(f'#{t} {min_max()}')

