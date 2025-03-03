# 사탕 게임
# 인접한 (좌, 하, 우) 2칸까지 자리 바꿔서 확인
# C : 빨간
# P : 파란
# Z : 초록
# Y : 노란
N = int(input())
ar = [list(input())+[0] for _ in range(N)] + [[0]*(N+1)]
color = ['C', 'P', 'Z', 'Y']
ar_t = list(map(list, zip(*ar)))


# 1차원 리스트에서 연속된 사탕의 수 중에 가장 큰 값을 리턴
def count(list):
    cnt = result = 1
    for i in range(1, len(list)):
        if list[i] == list[i-1]:
            cnt += 1
            result = max(result, cnt)
        else:
            cnt = 1
    return result


# 교환
def solve(ar):
    mx = 0
    for i in range(N-1):
        for j in range(0,N):
            # 오른쪽 사탕과 교환
            ar[i][j], ar[i][j+1] = ar[i][j+1], ar[i][j]
            mx = max(mx, count(ar[i]))
            ar[i][j], ar[i][j + 1] = ar[i][j + 1], ar[i][j]

            # 아래쪽 사탕과 교환
            ar[i][j], ar[i+1][j] = ar[i+1][j], ar[i][j]
            mx = max(mx, count(ar[i]), count(ar[i+1]))
            ar[i][j], ar[i + 1][j] = ar[i + 1][j], ar[i][j]
    return mx


result = max(solve(ar), solve(ar_t))
print(result)


