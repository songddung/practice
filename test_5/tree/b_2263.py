# 백준 2263 트리의 순회
# 인오더, 포스트오더가 주어지면 프리오더를 리턴
import sys
sys.setrecursionlimit(10**6)

def pre_order(in_s, in_e, po_s, po_e):
    if in_s > in_e or po_s > po_e:
        return

    p = post_order[po_e]
    print(p, end=' ')

    left = tree[p] - in_s
    right = in_e - tree[p]

    pre_order(in_s, in_s + left - 1, po_s, po_s + left - 1)
    pre_order(in_e - right+1, in_e, po_e-right, po_e - 1)

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
tree = [0] * (N+1)
for i in range(N):
    tree[in_order[i]] = i
pre_order(0, N-1, 0, N-1)
