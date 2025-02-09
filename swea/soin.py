sosu = [2,3,5,7,11]


def soin():
    n = int(input())
    count = [0] * 5

    for i in range(len(sosu)):
        while n % sosu[i] == 0:
                n = n // sosu[i]
                count[i] += 1

    return count

T = int(input())
for t in range(1,T+1):
    ar = soin()
    print(f'#{t}', *ar, sep=" ")
