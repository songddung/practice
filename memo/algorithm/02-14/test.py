# memoization
# memo = []  # 계산된 값을 저장할 리스트
# # n, m = map(int, input().split())  # 입력값
# n = int(input())
# cnt = 0
#
#
# def fibo(n):
#     global cnt
#     global memo  # 글로벌 변수 가져오기
#     cnt += 1
#     if n >= 2 and memo[n] == 0:  # n이 2보다 크고, memo[n]의 값이 0일때
#         memo[n] = fibo(n-1) + fibo(n-2)  # 저장
#     return memo[n]  # 리턴
#
#
# memo = [0] * (n+1)  # 0배열 선언
# memo[0] = 0
# memo[1] = 1
# print(fibo(n))
# print(cnt)
#
#
#
# # DP
# ### 피보나치 수 DP 적용
# cnt = 0
# def fibo2(n):
#     global cnt
#     cnt += 1
#     f = [0] * (n+1)
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n + 1):
#         f[i] = f[i-1] + f[i-2]
#     return f[n]
#
# print(fibo2(n))
# print(cnt)


# ### DFS
# v, e = map(int, input().split())
# ar = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# n = len(ar)
#
# def dfs(v, n):
#     adj_list = []
#     for i in range(e):
#         v, w = ar[i * 2], ar[i * 2 + 1]
#
#         adj_list[v].append(w)
#         adj_list[w].append(v)
#
#     visited = [0] * len(ar) + 1
#     stack = []
#
#     while True:
#         if visited[v] == 0:
#             visited[v] = 1
#             print(v)
#
#         for w in adj_list[v]:
#             if visited[w] == 0:
#                 stack.append(v)
#                 v = w
#                 break
#         else:
#             if stack:
#                 v = stack.pop()
#             else:
#                 break
#
#
#     adj_list = [[] for _ in range(v + 1)]

# dfs(v, n)

### 강사님
ar = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# g = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6]]
# v node하고 연결된 노드들은? g[v]
n = 7
g = [[] for _ in range(n+1)]
print(g)

for i in range(0, len(ar), 2):
    p1 = ar[i]
    p2 = ar[i+1]
    g[p1].append(p2)
    g[p2].append(p1)
print(g)

visited = [0] * (n+1)

def dfs_r(v):
    print(v)
    visited[v] = 1

    for w in g[v]:
        if not visited[w]:
            dfs_r(w)

dfs_r(1)

# def dfs(st):
#     stack = []
#     visited = [0] * (n+1)
#     stack.append(st)
#
#     while stack:
#         v = stack.pop(-1)  # stack에서 빼서 사용할 것
#
#         if not visited[v]:
#             print(v)
#             visited[v] = 1
#
#         for w in g[v]:
#             if not visited[w]:
#                 stack.append(w)


# def dfs(st):
#     stack = []
#     visited = [0] *(n+1)
#     stack.append(ar[0])
#
#     while stack:
#         v = stack.pop()
#         print(v, end=' ')
#
#         for w in g[v]:
#             if not visited[w]:
#                 stack.append(w)
#                 visited[w] = 1


