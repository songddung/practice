T = int(input())

def solve():
    N = int(input())
    arr = list(map(int, input()))
    result = 0
    max_num = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            result += 1

        else:
            if max_num < result:
                max_num = result
            result = 0
        if i == N-1:
            if max_num < result:
                max_num = result
    return  max_num


for t in range(1, T+1):
    print(f'#{t} {solve()}')