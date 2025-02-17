T = 10

def solve():
    for i in range(100, 0, -1):  # 가로 확인, 화문의 길이
        for j in range(100):  # 행
            for h in range(100 - i + 1):  # 열
                arr = []
                for k in range(i):  # i번 반복
                    arr.append(ar[j][h + k])
                if arr == arr[::-1]:  # 회문 확인
                    return i

def solve2():
    for i in range(100, 0, -1):
        for j in range(100):  # 열
            for h in range(100 - i + 1):  # 99라면 1 인덱스 0 반환
                arr = []
                for k in range(i):  # 행 i번 반복
                    arr.append(ar[h + k][j])
                if arr == arr[::-1]:  # 회문 확인
                    return i

for t in range(1, T + 1):
    tt = int(input())
    ar = [list(map(str, input())) for _ in range(100)]
    result1 = solve()
    result2 = solve2()
    if result1 > result2:
        print(f'#{tt} {result1}')
        # print('가로')
    else:
        print(f'#{tt} {result2}')
        # print('세로')


# i : 0 , k = 1