T = int(input())

def solve():
    n = int(input())
    ar = list(map(int, input().split()))

    for i in range(n-1):
        min_idx = i # 현재 인덱스를 최소인덱스로
        for j in range(i+1, n): # 현재값보다 1칸뒤부터 끝까지
            if ar[min_idx] > ar[j]: #현재 인덱스와 그뒤의 인덱스들을 하나씩 비교
                min_idx = j # 최소값 인덱스 찾기
        ar[i], ar[min_idx] = ar[min_idx], ar[i]

    return ar
for t in range(1,T+1):
    print(f'#{t}', end =' ')
    print(*solve())