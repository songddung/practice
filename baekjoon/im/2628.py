c , r = map(int, input().split())
row = [0, r]
col = [0, c]
n = int(input())


for _ in range(n):
    q , w = map(int, input().split())
    if q == 0:
        row.append(w)
    else:
        col.append(w)


col_mx = 0
col.sort()
for i in range(len(col)):
    if col_mx < col[i]-col[i-1]:
        col_mx = col[i]-col[i-1]



        
row_mx = 0
row.sort()
for i in range(len(row)):
    if row_mx < row[i]-row[i-1]:
        row_mx = row[i]-row[i-1]


print(col_mx*row_mx)