T = int(input())

# 1010
def solve():
    binary = list(map(int, input().strip()))
    binary_ar = []
    for i in range(len(binary)):
        check = binary[:i+1]  # i = 1일때 : 10
        txt =  binary[i+1:] # i = 0일때 : 10
        if check[i]:
            check[i] = 0
        else:
            check[i] = 1
        ar = ''
        for i in check:
            ar += str(i)
        for i in txt:
            ar += str(i)

        binary_ar.append(int(ar, 2))
        # print(binary_ar)



    ternary = list(map(int, input().strip()))
    ternary_ar = []
    # print(ternary)
    for j in range(len(ternary)):
        check = ternary[:j+1]
        txt = ternary[j+1:]

        if check[j]==0:
            ar = ''
            check[j] = 1
            for i in check:
                ar += str(i)
            for i in txt:
                ar += str(i)
            ternary_ar.append(int(ar, 3))
            ar = ''
            check[j] = 2
            for i in check:
                ar += str(i)
            for i in txt:
                ar += str(i)
            ternary_ar.append(int(ar, 3))

        elif check[j]==1:
            ar = ''
            check[j] = 0
            for i in check:
                ar += str(i)
            for i in txt:
                ar += str(i)
            ternary_ar.append(int(ar, 3))
            ar = ''
            check[j] = 2
            for i in check:
                ar += str(i)
            for i in txt:
                ar += str(i)
            ternary_ar.append(int(ar, 3))

        else:
            ar = ''
            check[j] = 1
            for i in check:
                ar += str(i)
            for i in txt:
                ar += str(i)
            ternary_ar.append(int(ar, 3))

            ar = ''
            check[j] = 0
            for i in check:
                ar += str(i)
            for i in txt:
                ar += str(i)
            ternary_ar.append(int(ar, 3))

    # print(ternary_ar)

    result = ''
    for i in binary_ar:
        if i in ternary_ar:
            result = i
            break
    return result

for t in range(1, T+1):
    print(f'#{t} {solve()}')


'''
1
1010
212
'''