T = int(input())

def solve():
    n = int(input())
    ar = list(map(int,input().split()))
    arr = [[], [], []]
    limit = n//2
    i = 1
    j = 0
    arr[0].append(ar[0])

    while i < n and j < 3:
        if ar[i] in arr[j]: # 소중대 리스트에 당근이 포함되어있는지 확인
            arr[j].append(ar[i]) #있으면 해당 리스트에 당근 추가
            i += 1
            if len(arr[j]) > limit: # 해당 리스트에 같은 당근 갯수가 리미트보다 크면 리턴
                return -1
        else: # 해당 당근이 포함되어있지 않다면
            if len(arr[j]) < limit:
                arr[j].append(ar[i])
            elif len(arr[j]) == limit:
                j += 1
            arr[j].append(ar[i])

        print(arr)

for t in range(1, T+1):
    solve()