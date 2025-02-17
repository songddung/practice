ar = [[0]*1001 for _ in range(1001)]

num = int(input())

for n in range(1, num+1):
    s2, s1, l2, l1 = map(int, input().split())

    for i in range(s1, s1+l1):
        for j in range(s2, s2+l2):
            ar[i][j] = n

for n in range(1, num+1):
    t = 0
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j] == n:
                t += 1
    if t :
        print(t)
    else:
        print(0)