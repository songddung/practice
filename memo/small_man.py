mans = []
while True :
    mans.append(int(input()))
    if len(mans) == 9 :
        break

sum_mans = sum(mans)

for i in mans :
    for j in range(len(mans)) :
        if i == j :
            pass
        if sum_mans - (i+j) == 100 :
            mans.remove(i)
            mans.remove(j)
print(sorted(mans))

