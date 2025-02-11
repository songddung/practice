T = 10

def solve():
    n = int(input())
    ar = []
    for i in range(8):
        ar.append(list(map(str, input())))
    count = 0
    # 가로 확인
    for i in range(8):
        for j in range(8-n+1):
            arr = []
            for k in range(n):
                arr.append(ar[i][j+k])
                # print(arr)
            if arr == arr[::-1]:
                count += 1

    # 세로 확인
    for j in range(8):
        for i in range(8-n+1):
            arr = []
            for k in range(n):
                arr.append(ar[i+k][j])
                # print(arr)
            if arr == arr[::-1]:
                count += 1

    return count

for t in range(1, T+1):
    print(f'#{t} {solve()}')