T = int(input())

def solve():
    n = int(input())
    ar = list(map(int,input().split())) # 당근 사이즈 리스트
    arr = [[], [], []] # 소 중 대
    limit = n//2

    i = 1
    j = 0
    ar.sort()
    arr[0].append(ar[0])

    while i < n and j < 3:
        if ar[i] in arr[j]: # 소중대 리스트에 당근이 포함되어있는지 확인
            arr[j].append(ar[i]) #있으면 해당 리스트에 당근 추가
            i += 1
            if len(arr[j]) == limit: # 해당 리스트에 같은 당근 갯수가 리미트보다 크거나 같으면 리턴
                return -1

        else: # 해당 당근이 포함되어있지 않다면
            if len(arr[j]) < limit-1: # 현재상자에 크기가 limit -1 보다 작을때
                arr[j].append(ar[i])
                i += 1
            else:
                j += 1
                arr[j].append(ar[i])
                i += 1

    min_num = len(arr[0])
    max_num = 0
    for i in arr:
        if max_num < len(i):
            max_num = len(i)
        if min_num > len(i):
            min_num = len(i)
    return max_num - min_num
for t in range(1, T+1):
    print(f'#{t} {solve()}')


