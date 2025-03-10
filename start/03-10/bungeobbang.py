# N : 인원
# M : 붕어빵 제작 시간
# K : M시간 당 K 개의 붕어빵 생성

T = int(input())


def solve():
    N, M, K = map(int, input().split())
    ar = list(map(int, input().split()))


    time = [0]* 11112
    check = 0

    for i in ar:
        time[i] += 1

    for i in range(11112):
        if i !=0 and i % M == 0:
            check += K

        check -= time[i]

        if check < 0:
            return 'Impossible'

    return 'Possible'



for t in range(1, T+1):
    print(f'#{t} {solve()}')