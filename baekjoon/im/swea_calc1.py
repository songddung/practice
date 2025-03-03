T = 10


def solve():
    N = int(input())
    text = input()
    num_ar = []
    str_ar = []

    # 후위 표기식 만들기
    for i in range(N):
        if text[i].isdigit():
            num_ar.append(text[i])
            if str_ar:
                plus = str_ar.pop()
                num_ar.append(plus)
        else:
            str_ar.append(text[i])

    # 후위 표기식 계산하기
    stack = []
    for i in num_ar:
        if i.isdigit():
            stack.append(int(i))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
    else:
        return stack.pop()
for t in range(1, T+1):
    print(f'#{t} {solve()}')