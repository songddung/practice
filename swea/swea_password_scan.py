hex = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '1',
    '4': '1',
    '5': '1',
    '6': '1',
    '7': '1',
    '8': '1',
    '9': '1',
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15',
}

T = int(input())


def solve():
    N, M = map(int, input().split())
    ar = [list(map(str, input().split())) for _ in range(N)]


for t in range(1, T+1):
    print(f'#{t} {solve()}')

