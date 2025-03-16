# # Rooted Binary Tree 재구성
#
# T = int(input())
#
#
# def make_tree(start, end, ar, result):
#     if start >= end:
#         return
#
#     p = (start + end) // 2  #부모
#     left = ar[(start + p - 1) // 2]  # 왼쪽 자식
#     right = ar[(p + end + 1) // 2]  # 오른쪽 자식
#     result[ar[p]] = [left, right]
#
#     make_tree(start, p-1, ar, result)
#     make_tree(p + 1, end, ar, result)
#
#
# def make_list(idx, root, tree, result, N):
#     if idx == N:
#         return 0
#     tree[idx].append(root)
#
#     if result[root] != 0:
#         for i in result[root]:
#             make_list(idx+1, i, tree, result, N)
#
#
#
#
# def solve():
#     N = int(input())
#     ar = list(map(int, input().split()))
#     root = ar[len(ar) // 2]
#     result = [0] * (2 ** N)
#     make_tree(0, len(ar)-1, ar, result)
#
#     tree = [[] for _ in range(N)]
#     make_list(0, root, tree, result, N)
#     return tree
#
#
# for t in range(1, T+1):
#     result = solve()
#     print(f'#{t}', end = ' ')
#     for i in result:
#         print(*i)

'''
3
3 2 7 5 6 1 4
'''


def in_order(root):
    global cnt
    if root <= depth:
        in_order(root * 2)
        tree[root] = arr[cnt]
        cnt += 1
        in_order(root * 2 + 1)


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    depth = 2 ** N - 1
    tree = [0] * (depth + 1)
    in_order(1)
    print(f"#{case} {tree[1]}")
    i = 2
    nodes = 2
    while i <= depth:
        print(" ".join(map(str, tree[i:i + nodes])))
        i += nodes
        nodes *= 2