# N : 컨테이너 수
# M : 트럭 수
# container : 화물 무게
# truck : 적재 용량


T = int(input())


def solve():
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    result = 0



    if truck[0] < container[-1]:
        return 0

    for i in truck:
        for j in container:
            if i >= j:
                result += j
                container.remove(j)
                break

    return result


for t in range(1, T+1):
    print(f'#{t} {solve()}')