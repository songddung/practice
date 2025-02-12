# ar = [[1,2,3],[4,5,6],[7,8,9]]
#
# print(ar[0:2][j])
# ar[0:2][:]  == [1,2,3]

t = 'TTTTTATTAATA'
p = 'TTA'
n = len(t)
m = len(p)
#
#
# i = j = 0
# while i < n and j < m:
#     if t[i] != p[j]:
#         i -= j + 1
#         j = 0
#     else:
#         i += 1
#         j += 1
# if j == m:
#     print(i-j)

count = 0

for i in range(n - m + 1): # 0 ~ 8
    txt = ''
    for j in range(m):
        txt += t[i+j]
        if txt == p:
            count += 1
            print(i)
print(count)



    # if t[i:i+m] == p:
    #     print(i)
