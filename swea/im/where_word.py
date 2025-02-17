T = int(input())

def solve():
    n, k = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(n)]
    result = 0


    for i in range(n): # 열
        count = 0
        for j in range(n):
            if ar[i][j]:
                count += 1
            else:
                if count == k:
                    result += 1
                count =0
        if count == k:
            result += 1

    for j in range(n): # 열
        count = 0
        for i in range(n):
            if ar[i][j]:
                count += 1
            else:
                if count == k:
                    result += 1
                count =0
        if count == k:
            result += 1

    return result
for t in range(1,T+1):
    print(f'#{t} {solve()}')