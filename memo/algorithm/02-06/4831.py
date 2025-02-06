### k : 최대주행거리
### N :  종점
### M : 충전기 개수
### 첫 K번 확인
### 다음 +K번 확인
# - 없으면 그전 인덱스 확인
def check():
    cnt = 0
    lastcharge = 0
    while lastcharge + K < N:
        if lastcharge+K in charge_stop:
            cnt += 1
            lastcharge = lastcharge + K
        else:
            for i in range(lastcharge+K-1, lastcharge, -1):
                if i in charge_stop:
                    cnt += 1
                    lastcharge = i
                    break
            else:
                return 0
    return cnt

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stop = [0] + list(map(int, input().split())) + [N] #충전기 있는 정류장

    print(f'#{tc} {check()}')