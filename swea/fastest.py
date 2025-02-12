# T = int(input())
#
# def solve():
#     t , p = map(str, input().split()) #  input
#     count = 0 # B 타이핑 횟수
#     k = 0 # B가 있으면 점프 할 숫자
#     for i in range(len(t)-len(p)+1): # 문자열의 길이 - 패턴의 길이 + 1
#         if i+k < len(t)-len(p)+1: #
#             if t[i+k] == p[0]:
#                 for j in range(1, len(p)):
#
#                     if t[i+j] != p[j]:
#                         break
#                 count += 1
#                 k += len(p)-1
#
#     if count == 0:
#         return len(t)
#     else:
#         le = count * len(p)
#         return len(t)-le + count
# for t in range(1,T+1):
#     print(f'#{t} {solve()}')


T = int(input())

def solve():
    t, p = map(str, input().split())  # input
    count = 0  # B 타이핑 횟수
    k = 0  # B가 있으면 점프 할 숫자
    i = 0  # 문자열 t의 인덱스

    while i <= len(t) - len(p):  # 문자열의 길이 - 패턴의 길이
        if t[i:i + len(p)] == p:  # 패턴이 발견되면
            count += 1
            i += len(p)  # 패턴의 길이만큼 점프
        else:
            i += 1  # 다음 문자로 이동

    if count == 0:
        return len(t)
    else:
        le = count * len(p)
        return len(t) - le + count

for t in range(1, T + 1):
    print(f'#{t} {solve()}')
