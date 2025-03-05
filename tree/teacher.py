# N = 13
# s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

# TREE = [[] for _ in range(N + 1)]
# ar = list(map(int, s.split()))
# for i in range(0, len(ar), 2):
#     p = ar[i]
#     c = ar[i+1]
#     TREE[p].append(c)
#
# print(TREE)
#
# def pre_order(root):
#     print(root)
#     if len(TREE[root]) > 0:
#         pre_order(TREE[root][0])
#     if len(TREE[root]) > 1:
#         pre_order(TREE[root][1])
#
# pre_order(1)
#
# print('=================')
# def in_order(root):
#     if len(TREE[root]) > 0:
#         in_order(TREE[root][0])
#     print(root)
#     if len(TREE[root]) > 1:
#         in_order(TREE[root][1])
#
# in_order(1)

# N = 13
# s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
# TREE = [[0, 0] for _ in range(N+1)]
# ar = list(map(int, s.split()))
# for i in range(0, len(ar), 2):
#     p = ar[i]
#     c = ar[i+1]
#     if TREE[p][0]:  # 왼쪽에 데이터가 있으면
#         TREE[p][1] = c
#     else:
#         TREE[p][0] = c
#
#
# def pre_order1(root):
#     print(root)
#     if TREE[root][0]:
#         pre_order1(TREE[root][0])
#     if TREE[root][1]:
#         pre_order1(TREE[root][1])
#
#
# pre_order1(1)
# print('=================================')
#
#
# def pre_order(root):
#     if root:
#         print(pre_order(TREE[root][0]))
#         print(pre_order(TREE[root][1]))
#
#
# def post_order(root):
#     if root:
#         post_order(TREE[root][0])
#         post_order(TREE[root][1])
#         print(root)
#
#
# post_order(1)

# N = 10
# TREE = [0] * (N+1)
# for i in range(N):
#     TREE[i+1] = chr(ord('A') + i)
# print(TREE)
#
#
# def pre_order(idx):
#     if idx < N:
#         print(TREE[idx])
#         pre_order(idx*2)
#         pre_order(idx * 2 + 1)
#
#
# pre_order(1)
# print('====================')
#
#
# def in_order(idx):
#     if idx <= N:
#         in_order(idx * 2)
#         print(TREE[idx])
#         in_order(idx * 2 + 1)
#
#
# in_order(1)


N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

child_l = [0] * (N+1)
child_r = [0] * (N+1)
par = [0] * (N+1)
ar = list(map(int, s.split()))
for i in range(0, len(ar), 2):
    p = ar[i]
    c = ar[i+1]
    par[c] = p
    if not child_l[p]:
        child_l[p] = c
    else:
        child_r[p] = c

print(child_l)
print(child_r)