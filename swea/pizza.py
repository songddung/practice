# T = int(input())
#
# def solve():
#     n, m = map(int, input().split())
#     ar = list(map(int, input().split()))
#     oven = [*ar[:n]]
#     turn = n  # 3
#     i = 0
#     check = [] # 현재 오븐에 있는 피자 번호
#     for w in range(n):
#         check.append(w)
#
#     while True:  # 오븐에 하나 남을때 까지
#
#         if len(oven) == 1:
#             return check[0]+1
#
#         idx = len(oven)
#         oven[i % idx] //= 2  # n으로 나누고 나머지
#
#         if oven[i % idx] == 0:  # 나눈값이 0이면
#             check.pop(i % idx)  # 해당 인덱스 빼기
#             oven.pop(i % idx)
#
#             if turn < m:  # 피자가 남았으면
#                 oven.insert(i % idx, ar[turn])  # 다음 피자로 변경
#                 check.insert(i % idx, turn)  # check에 추가
#                 turn += 1
#
#         i += 1
#         print(f'oven : {oven}')
#         print(f'check : {check}')
#
# for t in range(1, T+1):
#     print(f'#{t} {solve()}')

T = int(input())


def solve():
    n, m = map(int, input().split())
    ar = list(map(int, input().split()))
    oven = ar[:n]  # 처음 n개의 피자를 오븐에 넣음
    turn = n  # 다음 피자의 인덱스
    check = list(range(n))  # 피자의 인덱스를 저장하는 리스트

    while len(oven) > 1:  # 오븐에 하나 남을 때까지
        # 현재 피자의 치즈 양을 반으로 줄임
        oven[0] //= 2

        if oven[0] == 0:  # 치즈가 다 녹으면
            oven.pop(0)  # 피자 제거
            check.pop(0)  # 피자 번호 제거

            if turn < m:  # 다음 피자가 남아있으면
                oven.append(ar[turn])  # 다음 피자를 추가
                check.append(turn)  # 피자 번호 추가
                turn += 1  # 다음 피자 인덱스 증가
        else:
            # 피자를 오븐의 맨 뒤로 이동
            oven.append(oven.pop(0))
            check.append(check.pop(0))

    return check[0] + 1  # 1-based index로 반환


for t in range(1, T + 1):
    print(f'#{t} {solve()}')
