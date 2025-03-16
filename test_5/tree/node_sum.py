# swea 5178 노드의 합
T = int(input())


def post_order(n, N, tree):
    if n*2 <= N and n*2+1 > N:
        post_order(n*2, N, tree)
        post_order(n*2+1, N, tree)
        tree[n] = tree[n*2]

    elif n*2+1 <= N:
        post_order(n*2, N, tree)
        post_order(n*2+1, N, tree)
        tree[n] = tree[n*2] + tree[n*2+1]

def solve(t):
    N, M, L = map(int, input().split())  # 노드의 갯수, 리프노드의 갯수, 출력할 노드 번호
    tree = [0] * (N + 1)

    for _ in range(M):
        idx, v = map(int, input().split())
        tree[idx] = v

    post_order(1, N, tree)
    print(f'#{t} {tree[L]}')
    return

for t in range(1, T+1):
    solve(t)
