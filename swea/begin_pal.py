T = int(input())

def solve():
    text = input()

    if text == text[::-1]:
        return 1
    else:
        return 0

for t in range(1,T+1):
    print(f'#{t} {solve()}')