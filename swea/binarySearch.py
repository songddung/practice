T = int(input())

def solve():
    last, *ar = map(int, input().split())

    copy_last = last
    for i in range(len(ar)):
        count = 0
        start = 1
        last = copy_last

        while start <= last:
            count += 1
            middle = (start+last)//2

            if middle == ar[i]:
                break
            elif middle > ar[i]:
                last = middle
            else:
                start = middle
        ar[i] = count

    if ar[0] > ar[1]:
        return 'B'
    elif ar[0] < ar[1]:
        return 'A'
    else:
        return 0
for t in range(1,T+1):
    print(f'#{t} {solve()}')