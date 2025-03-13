# # 화물 토크
# T = int(input())
#
#
# def solve():
#     N = int(input())
#     visited = [0] * 25
#     result = 0
#     check_ar = []
#
#     for i in range(N):
#         st, ed = map(int, input().split())
#         check_ar.append((st, ed))
#
#     for i in range(len(check_ar)-1):
#         for j in range(len(check_ar)-1, i, -1):
#             if check_ar[i][1] - check_ar[i][0] > check_ar[j][1] - check_ar[j][0]:
#                 check_ar[i], check_ar[j] = check_ar[j], check_ar[i]
#
#     for st, ed in check_ar:
#         check = ed - st
#         if visited[st:ed].count(0) == check:
#             for j in range(st, ed):
#                 visited[j] = 1
#             result += 1
#
#     return result
#
#
# for t in range(1, T+1):
#     print(f'#{t} {solve()}')

# 화물 토크
def solve():
    N = int(input())  # 화물 개수
    visited = [0] * 25  # 25시간의 시간대 예약 여부, 최대 시간대가 25개라고 가정
    result = 0
    check_ar = []

    # 화물의 시작 시간과 종료 시간 입력 받기
    for i in range(N):
        st, ed = map(int, input().split())
        check_ar.append((st, ed))

    # 종료 시간 `ed` 기준으로 오름차순 정렬
    check_ar.sort(key=lambda x: x[1])

    # 각 화물을 배치 가능한지 확인
    for st, ed in check_ar:
        # 해당 구간에 예약이 되어 있지 않은지 확인
        if visited[st:ed].count(0) == ed - st:
            # 구간을 예약 처리
            for j in range(st, ed):
                visited[j] = 1
            result += 1

    return result

# 테스트 케이스 처리
T = int(input())  # 테스트 케이스 수
for t in range(1, T + 1):
    print(f'#{t} {solve()}')
