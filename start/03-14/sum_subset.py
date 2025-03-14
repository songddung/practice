T = int(input())


def solve(cnt, total):
    global result
    if total > M:
        return

    if cnt == N:
        if total == M:
            result += 1
        return
    solve(cnt+1, total)
    solve(cnt+1, total+ar[cnt])


for t in range(1, T+1):
    result = 0
    N, M = map(int, input().split())
    ar = list(map(int, input().split()))
    solve(0, 0)
    print(f'#{t} {result}')


# def solve(cnt, start):
#     global result
#     print(path)
#     if cnt > len(ar):
#         return
#
#     if sum(path) == M:
#         result += 1
#         return
#
#     for i in range(start, len(ar)):
#         path.append(ar[i])
#         solve(cnt+1, start+1)
#         path.pop()
