# 과목평가 2회차
- 3문항, 2시간 / 1, 2번 = 알고리즘 문제, 3번 서술형
- 범위 = 리스트 1, 2, 스트링
- 1, 3번 먼저 풀고 2번 풀기
- 부분점수 인정, 테케 최대한 맞추기, 3번은 틀린 설명이 없도록 작성

# 리스트 1
- 슬라이딩 윈도우
```python
처음 범위의 합 = sum(ar[:범위까지])
mx = 처음 범위의 합

for i in range(조사범위, 끝까지):
    처음 범위의 합 += ar[i] - ar[i - 범위] # 앞의 원소를 빼고 뒤의 원소를 더함
    mx = max(mx, 처음 범위의 합)
```
- DAT
- 구현, 시뮬
    - 소인수분해
    ```python
    def solve(l):
        n = int(input())
        c = [2, 3, 5, 7, 11]
        b = [0] * 5

        for i in range(len(c)):
            while n % c[i] == 0:
                n //= c[i]
                b[i] += 1

        print(f"#{l}", *b, sep=" ")
    ```
- Gravity
    - 배열 회전시키고 상자 떨구기
    ```python
    arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

    def gravity():
        n = len(arr)
        m = len(arr[0])

        for i in range(n - 1): # 5 - 1
            for j in range(m): # 3
                p = i
                # 현재칸이 아래로 내려갈 수 있다면 그 윗줄도 한 칸 씩 연쇄적으로 내려와야함
                while 0 <= p and arr[p][j] == 1 and arr[p + 1][j] == 0:
                    arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j]
                    p -= 1

    gravity()
    ```
- 버블정렬
```python
for i in range(n - 1, 0, -1):
    f = True # 최적화(이미 정렬되있으면 안함)

    for j in range(i):
        if ar[j] > a[j + 1]:
            ar[j], ar[j + 1] = ar[j + 1], ar[j]
            f = False # 최적화(이미 정렬되있으면 안함)
    if f: # 최적화(이미 정렬되있으면 안함)
        break
```
    - 서술형
        - 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
        - 정렬 과정
            1. 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
            2. 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
            3. 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 한다.
        - 장단점
            - 시간 복잡도 = O(n^2)
            - 코딩이 가장 손쉽다.
            - 가장 느리다. 평균, 최악 수행시간이 같음.
- 카운팅 정렬
```python
ar = [] # 정렬 전 배열
temp = [] # 정렬된 배열
count = [0] * (k + 1) # 정렬 전 배열 DAT

for i in range(len(ar)):
    count[ar[i]] += 1

for i in range(1, k + 1):
    count[i] += count[i - 1]

for i in range(len(ar) - 1, -1, -1):
    count[ar[i]] -= 1
    temp[count[ar[i]]] = ar[i]
```
    - 서술형
        - 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는 지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
        - 제한사항 = 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 = 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스되는 카운트들의 배열을 사용하기 때문이다.
        - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
        - 시간복잡도 = O(n + k) 길이 + 최대값
        - n이 비교적 작을 때만 가능.

- 순열 (동일한 숫자 포함 안된거)
    ```python
    for i in range(1, 4):
        for j in range(1, 4):
            if j != i:
                for k in range(1, 4):
                    if k != i and k != j:
                        print(i, j, k)
    ```
    - 베이비진 게임
- 그리디
    - 잔돈

# 리스트 2
- 행렬 전치
```python
for i in range(n):
    for j in range(n):
        if i < j:
            ar[i][j], ar[j][i] = ar[j][i], ar[i][j]
```
- 달팽이
```python
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n, m = int(input().split())
ar = [[0] * m for _ in range(n)]
y, x = 0, 0
c = 1
d = 0 # 0, 1, 2, 3

for _ in range(n * m):
    ar[y][x] = c

    # mn = 100000
    # mi, mj = 0, 0
    # for i in range(n):
    #     for j in range(m):
    #         if ar[i][j] < mn:
    #             mn = ar[i][j]
    #             mi, mj = i, j

    # ar[y][x] = mn
    # ar[mi][mj] = 1000000

    ny, nx = y + direct[d][0], x + direct[d][1]

    if 0 <= ny < n and 0 <= nx < m and ar[ny][nx] = 0:
        y, x = ny, nx
    else:
        d = (d + 1) % 4
        y, x = y + direct[d][0], x + direct[d][1]
    
    c += 1
```
- 부분집합
    - n개 배열에서 나올 수 있는 부분집합의 수 = 2^n
```python
ar = [3, 6, 7, 1, 5, 4]
n = len(ar)

# n을 2진법으로 바꾼 것에 대한 i = i가 2진법으로 모든 경우의 수가 나옴.
for i in range(1 << n):
    t = []

    for j in range(n):
        if i & (1 << j):
            t.append(ar[j])
    print(t)
```
- 이진탐색
```python
def binarySearch(ar, n, key):
    start = 0
    end = n - 1

    while start <= end:
        middle = (start + end) // 2

        if ar[middle] == key:
            return middle
        elif ar[middle] > key:
            end = middle - 1
        else:
            start = middle + 1

    return False
```
- 선택정렬
    - k번째로 작은 원소 찾기 = k만큼만 선택 정렬.

# 스트링
- 아스키
    - 공백 = 32
    - 대문자 > 소문자 = +32
    - 소문자 > 대문자 = -32
    - 숫자 0~9 = 48~57
    - A~Z = 65~90
    - a~z = 97~122
    - 알파벳 갯수 세는 DAT = `b = [0] * 123`, `b[ord(arr[i])] += 1`
- 회문
```python
def solve(ar, l):
    for i in ar:
        for j in range(n - l + 1):
            for k in range(l // 2):
                if i[j + k] != i[j + l - 1 - k]:
                    break
            else:
                return True

    return False
```
- atoi()
```python
def atoi(s):
    i = 0

    for x in s:
        i = i * 10 + ord(x) - ord('0')

    return i
```
- zip = `[list(r) for r in zip(*ar)]`