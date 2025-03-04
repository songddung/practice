# 수열
# 슬라이딩 윈도우 필요
# N, K = 전체 날짜 수, 연속하는 날짜 수


# N, K = map(int, input().split())
# ar = list(map(int, input().split()))
#
# def solve(ar, n, k):
#     mx = sum(ar[:k]) # 연속하는 날짜의 온도최대값
#
#     start = sum(ar[:k]) # 초기 범위
#
#     for i in range(k, n):
#
#         start = start - ar[i-k] + ar[i]
#
#         mx = max(mx, start)
#     return mx
#
# print(solve(ar, N, K))

N, K = map(int, input().split())
ar = list(map(int, input().split()))

start = sum(ar[:K])
mx = 0
for i in range(K, N):

    start = start - ar[i-K] + ar[i]
    mx = max(mx, start)

print(mx)
























