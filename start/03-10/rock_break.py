# DFS + BFS
# 모든 경우의 수를 확인

T = int(input())

def blocks(cnt, remain, ar, N, W, H):
    global result
    if cnt == N or remain == 0:
        result = min(result, remain)
        return

    for x in range(W):
        copy_ar = [row[:] for row in ar]


def solve():
    N, W, H = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(H)]
    remain = 0
    result = 9*12*15
    for i in range(H):
        for j in range(W):
            if ar[i][j]:
                remain += 1
    blocks(0, remain, ar, N, W, H)


for t in range(1, T+1):
    print(f'#{t} {solve()}')