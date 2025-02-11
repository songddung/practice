T = int(input())

def solve():
    ar = [list(map(str, input())) for _ in range(5)]

    arr = []
    for j in range(16):
        for i in range(5):
            if len(ar[i])-1 >= j: # j가  ar의 리스트의 0번째 리스트의 길이 보다 작거나 같을때
                arr.append(ar[i][j])
    return arr
for t in range(1,T+1):
    print(f'#{t}', end=' ')
    print(*solve(), sep='')
