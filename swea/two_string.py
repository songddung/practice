T = int(input())

def solve():
    n, m = map(int, input().split())
    ar = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    len_ar = len(ar)
    len_arr = len(arr)
    max_num = 0

    if len_ar < len_arr:
        for i in range(len_arr - len_ar + 1):
            # print(i)
            t = 0
            for j in range(len_ar):
                # print(j)
                t += arr[i+j] * ar[j]
                # print(t)
            if max_num < t:
                max_num = t
    else:
        for i in range(len_ar - len_arr + 1):
            # print(i)
            t = 0
            for j in range(len_arr):
                # print(j)
                t += ar[i + j] * arr[j]
            if max_num < t:
                max_num = t

    return max_num

for t in range(1, T+1):
    print(f'#{t} {solve()}')