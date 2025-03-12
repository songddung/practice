# 카드 5장
# 연속된 3장 갯수
card = ['A', 'J', 'Q', 'K']
path = []
result = 0


def cnt_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True


def recur(cnt):
    global result
    if cnt == 5:
        if cnt_three():
            result += 1
            print(path)
        return

    for i in range(4):
        path.append(card[i])
        recur(cnt + 1)
        path.pop()


recur(0)
print(result)