from collections import deque

direct = ((-1, 0), (0, 1), (1, 0), (0, -1))


def dfs(st, graph):
    s = deque([st])
    visited = [False] * len(graph)

    while s:
        v = s.pop()

        for w in graph[v]:
            if not visited[w]:
                s.append(w)
                visited[w] = True

    return visited.count(True)


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    graph2 = [[] for _ in range(n + 1)]

    r = 0

    for _ in range(m):
        n1, n2 = map(int, input().split())

        graph[n1].append(n2)
        graph2[n2].append(n1)

    for i in range(1, n + 1):
        c1 = dfs(i, graph)
        c2 = dfs(i, graph2)

        if c1 + c2 == n - 1:
            r += 1

    print(r)


if __name__ == "__main__":
    main()