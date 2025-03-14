# 수영장


### 완전탐색
# T = int(input())
#
#
# def solve(cnt, cost):
#     global result
#
#     if result < cost:
#         return
#
#     if cnt > 12:
#         result = min(result, cost)
#         return
#
#     # 하루권
#     solve(cnt + 1, cost + month[cnt]*costs[0])
#
#     # 한달권
#     solve(cnt + 1, cost + costs[1])
#
#     # 3달권
#     solve(cnt + 3, cost + costs[2])
#
#
# for t in range(1, T+1):
#     costs = list(map(int, input().split()))
#     month = [0] + list(map(int, input().split()))
#     result = max(costs)
#
#     solve(1, 0)
#     print(f'#{t} {result}')



### DP
# 문제제 접근법
# 하향 : TOP_DOWN
#   - DP(메모이제이션)
#   - 거듭제곱

# 상향식 : BOTTOM-UP
#   - 시작점을 정해둔다
#   - 앞으로 쌓아 나가면서 진행
#       - 기존 값을 활용
#       - 정답을 계산해서 저장하면서 진행
#   => 점화식을 구하는 경우가 많다

T = int(input())


def solve():
    dp = [0] * 13
    dp[1] = min(costs[0] * month[1], costs[1])
    dp[2] = dp[1] + min(costs[0] * month[2], costs[1])

    for m in range(3, 13):
        # N월의 최소 비용 훗보
        # 1. (N-3)월에 3개월 이용권을 구입한 경우
        # 2. (N-1)월의 최소 비용 + 1일권 구매
        # 3. (N-1)월의 최소 비용 + 1달권 구매
        dp[m] = min(dp[m-3] + costs[2],
                    dp[m-1] + (month[m] * costs[0]),
                    dp[m-1] + costs[1])

    return min(dp[12], costs[3])


for t in range(1, T+1):
    costs = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    print(f'#{t} {solve()}')
