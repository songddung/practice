T = int(input())
pw = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

def solve():
    N, M = map(int, input().split())
    ar = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        if ar[i].count(1) > 0:
            ar = ar[i]
            break


    check = 0
    for i in range(M-1, -1, -1):

        if ar[i] == 1:
            # print(i)
            password = ar[i-55:i+1]
            break
    # print(len(password))

    dc = []
    for i in range(0, len(password), 7):
        st = ''
        for i in password[i:i+7]:
            st += str(i)
        # print(st)

        dc.append(pw[st])

    odd = []
    even = []
    for i in range(1, 9):
        if i % 2 == 0:
            even.append(dc[i-1])
        else:
            odd.append(dc[i-1])

    # print(odd, even)
    if ((sum(odd) * 3) + sum(even)) %10 == 0:
        return sum(odd)+sum(even)
    else:
        return 0

for t in range(1, T+1):
    print(f'#{t} {solve()}')


'''
0000000000000000000000010111100011010111011001100101110110111011011101100110010000000000000000000000 
'''