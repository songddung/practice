### 정류장 5000개 1~5000
### 노선 N개
### i번째 버스 노선은 Ai이상 Bi이하인 모든 정류장만을 다님 1~3, 2~5
### P개의 버스 정류장에 대해 각정류장에 몇개의 버스 노선이 다니는지 구하라
### 정류장번호 1,2,3,4,5

T = int(input()) # 테스트 케이스 수

def solve():
    case = int(input()) # 노선 범위 수
    arr = [list(map(int, input().split())) for _ in range(case)] # 노선 리스트
    stop = int(input()) # 정류장 번호 갯수
    check = [int(input()) for _ in range(stop)] # 정류장 번호
    ar = [0] * stop


    for j in range(case): # 노선수 만큼
        for k in range(arr[j][0], arr[j][1]+1): # 노선범위
            for i in range(len(check)):  # 체크해야하는 정류장 갯수만큼
                if k == check[i]:
                    ar[i] += 1
    return  ar
for t in range(1, T+1):

    print(f'#{t}', *solve(), sep=" ")