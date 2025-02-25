mans = []
while True :
    mans.append(int(input()))
    if len(mans) == 9 :
        print(mans)
        break

sum_mans = sum(mans)

for i in mans :
    for j in range(len(mans)) :
        print(f'j : {j}')
        if i == mans[j] :
            continue
        if sum_mans - (i+mans[j]) == 100 :
            mans.remove(i)
            mans.remove(mans[j-1])
            break
print(sorted(mans))

