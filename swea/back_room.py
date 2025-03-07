T = int(input())


def solve():
    ar = [0] * 200
    N = int(input())

    for i in range(N):
        start, end = map(int, input().split())

        start = (start+1) // 2
        end = (end+1)//2

        if start > end:
            start, end = end, start

        for j in range(start-1, end):
            ar[j] += 1

    return max(ar)
for t in range(1, T+1):
    print(f'#{t} {solve()}')

'''
3  
4  
10 20 
30 40
50 60
70 80
2 
1 3
2 200
3
10 100
20 80
30 50
'''