#  이진수 표현
# N : N자리부터 마지막까지 1인지 확인
# M : 2진수로 바꿔서
T = int(input())


def solve():
    N, M = map(int, input().split())
    target = M
    for i in range(N):  # N번 확인
        if target & 0x1 == 0:  #  맨 우측 비트가 1인 지 체크 : !비트연산이라는 것을 명시하기 위해 0x1을 주로 사용
            return False
        target = target >> 1  # 맨 우측 비트를 삭제


# 단순 접근
# def solve2():
#     N, M = map(int, input().split())
#     mask = (1 << N) - 1
#     result = (M & mask) == mask
#     return result

for t in range(1, T+1):
    print(f'#{t} {"ON" if solve() is None else "OFF"}')