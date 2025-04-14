T = int(input())


def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = len(lst)//2
    left = [x for x in lst if x < lst[pivot]]
    middle = [x for x in lst if x == lst[pivot]]
    right = [x for x in lst if x > lst[pivot]]
    return quick_sort(left) + middle + quick_sort(right)

def solve():
    N = int(input())
    ar = list(map(int, input().split()))
    return quick_sort(ar)[N//2]


for t in range(1, T+1):
    print(f'#{t} {solve()}')