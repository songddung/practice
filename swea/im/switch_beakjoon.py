def solve():
    t = int(input())
    ar = list(map(int, input().split()))
    gender = []
    n = int(input())
    for i in range(n):
        gender.append(list(map(int, input().split())))

    for j in gender:

        gen, num = j[0], j[1]

        if gen == 1:  # 남자 일 때
            for k in range(num, t+1, num):
                ar[k-1] = 1 - ar[k-1]


        if gen == 2: ## 여자일 때
            i = 0

            while 0 <= num-1-i and num-1+i < len(ar):
                    if ar[num-1-i] == ar[num-1+i]:
                        i +=1

                    else:
                        break

            ar[num-1] = 1 - ar[num-1]

            for h in range(1, i):
                ar[num-1+h] = 1 - ar[num - 1 + h]
                ar[num - 1 - h] = 1 - ar[num - 1 - h]

    return ar

result = solve()
if len(result) <= 20:
    print(*result)
else:
    for i in range(0, len(result), 20):
        print(*result[i:i+20])

