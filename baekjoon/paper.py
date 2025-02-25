### 색종이
# 100 * 100 도화지
# 10 * 10 색종이
# 색종이 넓이 구하기


input1 = int(input())
input2 = []
for i in range(input1) :
    input2.append(list(map(int,input().split())))



arr = [[0] * 101 for i in range(101)]


for i in input2 :
    for x in range(10) :
        for y in range(10) :
            arr[i[1]+y][i[0]+x] = 1


check = 0
for i in range(101):
    check += arr[i].count(1)

print(check)