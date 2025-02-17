T = 10

def solve():
    tc, road = map(int, input().split())
    ar = list(map(int, input().split()))
    # len_ar = len(ar)
    start = 0
    end = 99
    # print(ar)

    line = [[] for _ in range(99)]

    for i in range(0, len(ar), 2):
        f = ar[i]
        g = ar[i+1]

        line[f].append(g)

    st = [0]
    visited = [0] * 100
    visited[0] = 1

    while st:
        check = st.pop()
        if check == end:
            return 1
        for w in line[check]:
            if not visited[w]:
                visited[w] = 1
                st.append(w)

    return 0




for t in range(1, T+1):
    print(f'#{t} {solve()}')