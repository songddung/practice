r, c = map(int, input().split())
ar = []
arr = [[-1] * c for _ in range(r)]
for i in range(r):
    ar.append(list(map(str, input())))

for i in range(r):
    check = 0
    add_n = 1
    for j in range(c):
        if check == 1:
            arr[i][j] = add_n
            add_n += 1
        if ar[i][j] == 'c':
            arr[i][j] = 0
            check = 1
            add_n = 1


for i in range(len(arr)):
    print(*arr[i])