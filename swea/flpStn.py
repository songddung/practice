T = int(input())

def solve():
    N, m = map(int, input().split())
    ar = [-1]+ list(map(int, input().split()))
    change = []
    for i in range(m):
        change.append(list(map(int, input().split())))


    for n in change:
        start = ar[n[0]-1]
        for k in range(n[0], n[0]+n[1]-1): # 내 위치 다음부터 내위치 인덱스+뒤집을 갯수 ( 2,2 라면 내위치 인덱스는 1,
                                                                                        # 내 위치 다음 인덱스 2
                                                                                        # 4까지면 인덱스 3번
                                                                                        # 2, 3이 나옴
            if k < N: # 현재위치 + 뒤집을 돌 갯수 카운트 가 N보다 작을때 까지
                ar[k] = start # 현재위치 + 카운트 = 현재위치돌로 변경
    return ar

for t in range(1,T+1):
    print(f'#{t}', end=' ')
    print(*solve())