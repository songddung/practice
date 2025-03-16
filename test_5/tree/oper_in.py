# # 사칙연산, 중위순회

T = 10


def solve(node):
    if node:
        solve(sub[node][0])
        solve(sub[node][1])

        if str(tree[node]).isdigit():
            result.append(tree[node])
        else:
            a = result.pop()
            b = result.pop()

            if tree[node] == '+':
                result.append(b + a)
            elif tree[node] == '-':
                result.append(b - a)
            elif tree[node] == '/':
                result.append(b // a)
            elif tree[node] == '*':
                result.append(b * a)

for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    sub = [[0,0] for _ in range(N+1)]
    for _ in range(N):
        idx, v, *ar = map(str, input().split())
        idx = int(idx)
        if ar:
            tree[idx] = v
            sub[idx][0] = int(ar[0])
            sub[idx][1] = int(ar[1])
        else:
            tree[idx] = int(v)
    result = []
    solve(1)

    print(f'#{t} {result.pop()}')

'''
7
1 / 2 3
2 - 4 5
3 - 6 7
4 261
5 61
6 81
7 71
'''


# def post_order(n):
#     if n:
#         a = post_order(L[n])
#         b = post_order(R[n])
#
#         if TREE[n] == '+':
#             TREE[n] = a + b
#         elif TREE[n] == '-':
#             TREE[n] = a - b
#         elif TREE[n] == '*':
#             TREE[n] = a * b
#         elif TREE[n] == '/':
#             TREE[n] = a // b
#
#         return TREE[n]
#
#
# T = 10
# for tc in range(1, T + 1):
#     N = int(input())
#     cal = [input().split() for _ in range(N)]
#     TREE = [0] * (N + 1)
#     L = [0] * (N + 1)
#     R = [0] * (N + 1)
#
#     for i in range(N):
#         if len(cal[i]) == 4:
#             TREE[int(cal[i][0])] = cal[i][1]
#             L[int(cal[i][0])] = int(cal[i][2])
#             R[int(cal[i][0])] = int(cal[i][3])
#         elif len(cal[i]) == 2:
#             TREE[int(cal[i][0])] = int(cal[i][1])
#     print(TREE)
#     print(L)
#     print(R)
#     post_order(1)
#     print(f'#{tc} {TREE[1]}')
