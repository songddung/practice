T = 10


def solve():
    result = []
    q = []
    for i in range(1, V+1):
        if In[i] == 0:
            q.append(i)

    while q:
        v = q.pop(0)
        result.append(v)

        for i in range(V+1):
            if g[v][i]:
                In[i] -= 1
                if In[i] == 0:
                    q.append(i)
    return result


for t in range(1, T+1):
    V, E = map(int, input().split())
    ar = list(map(int, input().split()))

    g = [[0] * (V+1) for _ in range(V+1)]
    In = [0] * (V+1)
    for i in range(0, len(ar), 2):
        st = ar[i]
        ed = ar[i+1]
        g[st][ed] = 1
        In[ed] += 1
    print(f'#{t}', *solve())
