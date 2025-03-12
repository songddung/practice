# baby-gin
# 6자리 숫자를 입력
# 검사
#   숫자 3개가 연속?
#   숫자 3개가 같음?
# 모든 조합 > 순열
'''
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''

used = [0] * 6

def is_baby_gin():
    cnt = 0
    a,b,c = path[0], path[1], path[2]
    if a == b == c:
        cnt += 1
    elif a == (b-1) == (c-2):
        cnt += 1

    d,e,f = path[3], path[4], path[5]
    if d == e == f:
        cnt += 1
    elif d == (e-1) == (f-2):
        cnt += 1

    return cnt == 2


baby_gin_result = False


def recur(cnt):
    global baby_gin_result
    if cnt == 6:
        if is_baby_gin():
            baby_gin_result = True
        print(path)
        return

    for i in range(6):
        # i를 썻다면 뽑기x
        if used[i]:
            continue

        used[i] = 1
        path.append(ar[i])
        recur(cnt + 1)
        path.pop()
        used[i] = 0

ar = list(map(int, input().split()))
path = []
recur(0)

print('baby_gin') if baby_gin_result else print('No')
