n = 9

ar = []
for i in range(n):
    ar.append(int(input()))

def solve(ar):

    for i in range(len(ar)):
        for j in range(1, len(ar)):
            if ar[i] != ar[j]:
                if sum(ar) - (ar[i]+ar[j]) == 100:
                    num1 = ar[i]
                    num2 = ar[j]
                    ar.remove(num1)
                    ar.remove(num2)

                    return ar
arr = solve(ar)
arr.sort()
for i in arr:
    print(i)