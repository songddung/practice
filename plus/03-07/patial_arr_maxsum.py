N, M, K = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]
mx = 0
idx = ''
for i in range(N-K+1):
    for j in range(M-K+1):



        num = 0
        for k in range(K):

            num += sum(ar[i + k][j:j + K])
        if mx < num:
            mx = num

            idx = '('+str(i+1)+','+str(j+1)+')'

print(f'최대 부분합: {mx}')
print(f'최대 부분합의 좌상단 위치: {idx}')