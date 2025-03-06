N = 1000000
a = [False, False] + [True]*(N-1)
primes=[]
# print(a[0])
# print(a[1])
for i in range(2,N+1): # 2부터 100만1까지
    if a[i]: #
        primes.append(i)
        # primes += str(i)+' '
        # print(i, end=' ')
        # print(i, end = " ")

        for j in range(i*i, N+1, i): # 찾은 소수를 제외한 소수의 모든 배수를 False로 바꿈
            a[j] = False

print(*primes)


