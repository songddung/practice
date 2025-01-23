N = int(input())
input2 = list(map(int,input().split()))
line_list = []


for i in range(1,N+1) :
    if i == 1 :
        line_list.append(i)
      
    else :
        line_list.insert(input2[(i-1)], i)
      
print(list(reversed(line_list)))



