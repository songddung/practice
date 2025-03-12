# 완전탐색
# 주사위 3개 던져 합 10 이하인 개수 출력
# 종료조건 : 3번 던진다
# 나올 수 있는 범위 1~6

path = []
result = 0


def recur(cnt, total):
    global result

    if total > 10:  # << 가지치기 : 효율 상승
        return

    if cnt == 3:
        # if total <= 10:  # path의 길이만큼 반복 > 비효율
        result += 1
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        recur(cnt + 1, total + i)
        path.pop()


recur(0, 0)
print(result)