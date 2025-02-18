### 강사님 부분집합

n = 3
ar = [10, 21, 22]
result = [-1, -1, -1]


def subsets(k):
    if k == 3:
        t = 0
        for i in range(n):
            if result[i]:
                t += ar[i]

        print(result, '=>', t)
        if t == 10:
            for i in range(n):
                if result[i]:
                    print(ar[i], end=',')
            print()

        return

    candidates =[1, 0]
    for i in candidates:
        result[k] = i
        subsets(k+1)


subsets(0)


### 순열
n = 3
ar = [1, 12, 3, 4, 5]

def per_1(k):
    if k == n:
        print(result)
        return

    candidates = []
    for i in range(n):
        if i not in result[0:k]:
            candidates.append(i)

    for i in candidates:
        result[k] = i
        per_1(k+1)


visited = [-1] * n
def per(k):
    if k == n:
        print(result)
        return

    for i in range(n):
        if not visited[i]:
            result[k] = i
            visited[i] = True
            per(k+1)
            visited[i] = False
