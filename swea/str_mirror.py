T = int(input())

mirror = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}

def solve():
    text = input()[::-1]
    ar = []
    for i in text:
        ar.append(mirror[i])
    return ar
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    print(*solve(), sep='')