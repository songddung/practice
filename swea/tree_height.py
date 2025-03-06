# 나무 높이
# N = 나무갯수
# ar = 나무리스트


T = int(input())


def solve():
    N = int(input())
    ar = list(map(int, input().split()))
    # print(ar)
    i = 1
    while True:
        mx = max(ar)
        mn = min(ar)
        midx = ar.index(mn)
        if mx == mn:  # 제일 큰 나무가 제일 작은 나무가 같을때
            return i-1
        if mx-mn > 2:

            ar[midx] += i%2
        elif mx-mn == 2:
            if i%2 == 0 :
                ar[midx] += 2
            else:
                i += 1
                continue
        elif mx-mn == 1:
            if i%2 == 0:
                i += 1
                continue
            else:
                ar[midx] += i%2
        else:
            ar[midx] += i%2
        i += 1



for t in range(1, T+1):
    print(f'#{t} {solve()}')