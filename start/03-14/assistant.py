T = int(input())

score = {
    0: 'A+',
    1: 'A0',
    2: 'A-',
    3: 'B+',
    4: 'B0',
    5: 'B-',
    6: 'C+',
    7: 'C0',
    8: 'C-',
    9: 'D0'
}


def solve():
    n, k = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(n)]
    arr = []
    p = n//10

    for i in range(len(ar)):
        num = ar[i][0] * 0.35 + ar[i][1] * 0.45 + ar[i][2] * 0.2
        arr.append((num, i))
    arr.sort(reverse=True)

    for i in range(len(arr)):
        if arr[i][1] == k-1:
            return score[i // p]


for t in range(1, T+1):
    print(f'#{t} {solve()}')
