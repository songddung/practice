# v = 노드 개수
# e = 간선 수
# s = 출발 노드
# g = 도착 노드

T = int(input())

def solve():
    v, e = map(int, input().split())

    ar_e = []  # 간선 리스트

    for i in range(e):
        ar_e.append(list(map(int, input().split())))
    # print(ar_e)

    s, g = map(int, input().split())  # 시작점, 끝점

    ar = [[] for _ in range(v + 1)]  # 빈배열 생성

    # print(ar)

    for i, j in ar_e:  # 연결리스트 생성
        ar[i].append(j)

    # print(ar)

    st = [s]  # 시작
    visited = [0] * (v+1)  # 이동확인
    visited[s] = 1 # 시작은 다시 안가게

    while st:
        check = st.pop()  # 연결된 노드 뽑아서 확인하기
        if check == g:  #연결되어있으면 리턴
            return 1
        for i in ar[check]: #
            if not visited[i]:
                visited[i] = 1
                st.append(i)

    return 0

for t in range(1, T+1):
    print(f'#{t} {solve()}')