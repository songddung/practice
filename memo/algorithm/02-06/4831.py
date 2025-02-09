### k : 최대주행거리
### N :  종점
### M : 충전기 개수
### 첫 K번 확인
### 다음 +K번 확인
# - 없으면 그전 인덱스 확인
def check():
    cnt = 0 # 충전 횟수
    lastcharge = 0 # 마지막 충전 위치
    while lastcharge + K < N: # 마지막충전 위치 + 최대 주행거리가 종점보다 작을 때
        if lastcharge+K in charge_stop: # 마지막충전 위치 + 최대 주행거리가 충전기가 있는 정류장에 포함될 때
            cnt += 1 # 충전 횟수 증가
            lastcharge = lastcharge + K # 마지막 충전위치를 현재 위치로 변경
        else:
            for i in range(lastcharge+K-1, lastcharge, -1): # 마지막 충전위치 + 주행거리 -1 부터 마지막 충전위치까지 거꾸로 추출 > 3+3-1부터 3까지 : 5,4
                if i in charge_stop: # 위치에 충전기가 있을 떄
                    cnt += 1 # 충전 횟수 증가
                    lastcharge = i # 마지막 충전위치를 현재 위치로
                    break # 반복문 탈출
            else: # for문을 다돌았는데 충전기가 없으면
                return 0 # 0리턴
    return cnt # while문을 다돌면 cnt 반환

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stop = [0] + list(map(int, input().split())) + [N] #충전기 있는 정류장

    print(f'#{tc} {check()}')