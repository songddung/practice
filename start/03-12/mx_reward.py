# swea 최대상금

T = int(input())


def solve(n):  # 파라미터 : 교환 횟수
    global result
    if n == N:  # 다 바꾸면
        result = max(result, int("".join(map(str, lst))))  # result = result랑 바꾼 문자열이랑중에 큰거
        return

    for i in range(L-1):  # 마지막전꺼까지
        for j in range(i+1, L):  # i 다음부터 마지막까지
            lst[i], lst[j] = lst[j], lst[i]  # 교환
            check = int("".join(map(str, lst)))  # 리스트를 숫자로 바꿔
            # if (n, check) not in visited:  # 방문여부 리스트에 해당 숫자열이 없으면 재귀 호출
            if (n, check) not in visited:
                solve(n+1)
                # visited.append((n,check))  # 호출하고 방문여부 리스트에 넣기
                visited[(n, check)] = 1
            lst[i], lst[j] = lst[j], lst[i]  # 바꾼 숫자 복귀


for tc in range(1, T + 1):
    st, t = input().split()  # 숫자열, 교환 횟수
    N = int(t)
    lst = [] # 문자열을 리스트에 넣을거임
    for p in st:
        lst.append(int(p))

    L = len(lst) # 리스트 길이
    result = 0  # 반환 숫자열
    visited = {}  # 방문 여부 판단
    solve(0)
    print(f'#{tc} {result}')