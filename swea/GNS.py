T = int(input())

my_dict = {
    "ZRO" : 0,
    "ONE" : 1,
    "TWO" : 2,
    "THR" : 3,
    "FOR" : 4,
    "FIV" : 5,
    "SIX" : 6,
    "SVN" : 7,
    "EGT" : 8,
    "NIN" : 9
}
def solve():
    cn = input()
    ar = list(map(str, input().split()))
    t_num = int(cn.split(' ')[1]) # 7041 글자수
    arr = [0]*10 # dat list == [[400], [300], [0], [0], [0], [0], [0], [0], [0], [0]]

    for i in range(t_num):
        arr[my_dict[ar[i]]] += 1

    result = []
    my_arr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for i in range(len(arr)):
        for j in range(arr[i]):
            result.append(my_arr[i])
    return result

for t in range(1,T+1):
    print(f'#{t} ')
    print(*solve())
