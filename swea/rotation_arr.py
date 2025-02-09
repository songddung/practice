T = int(input())

def solve():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = []
    # 90도
    ar = []
    for i in range(N):
        for j in range(N-1,-1,-1):
          ar.append(arr[j][i])
    total.append(ar)
    # 180도
    ar = []
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):

            ar.append(arr[i][j])
    total.append(ar)
    # 270도
    ar = []
    for i in range(N-1,-1,-1):
        for j in range(N):
          ar.append(arr[j][i])
    total.append(ar)



    for k in range(0, len(total[0]), N):
        for i in range(3):
            ar = []
            for j in range(N):

                print(total[i][j+k], end='')

            print(end=' ')
        print()





for t in range(1, T+1):
    print(f'#{t}')
    solve()