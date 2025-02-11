T = int(input())

def solve():
    n = input()
    m = input()
    my_dict = {}

    for i in n:
        count = 0
        for j in m:
            if i == j:
                count += 1
        my_dict[i] = count
    max_num = 0
    for k, v in my_dict.items():
        if v > max_num:
            max_num = v

    return max_num


for t in range(1,T+1):
    print(f'#{t} {solve()}')