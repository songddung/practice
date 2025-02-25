'''
n개의 원소로 이루어져 있는 수열 a의 정보와, m개의 원소로 이루어져 있는 수열 b의 정보가 주어졌을 때 수열 b가 수열 a의 연속부분수열인지를 판단하는 프로그램을 작성해보세요.

수열 b가 수열 a의 원소들을 연속하게 뽑았을 때 나올 수 있는 수열이라면 연속부분수열이라 부릅니다.

예를 들어, 수열 a가 [1, 5, 2, 6]일 때, 수열 b가 [5, 2]라면 연속부분수열이지만, 만약 수열 b가 [5, 6]이라면 연속부분수열이 아닙니다.

'''

n1 , n2 = list(map(int, input().split()))
input2 = list(map(int, input().split()))
input3 = list(map(int, input().split()))


def solve(arr1, arr2) :
        
    for i in range(n1-n2+1) :
        check = None
        for j in range(len(arr2)) :
            if arr1[i+j] == arr2[j] :
                continue
            else : 
                check = False
        if check != False :
            return True
    return check


result = solve(input2,input3)

if result == False :
    print('No')
else :
    print('Yes')
        
