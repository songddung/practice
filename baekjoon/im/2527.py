# 직사각형
# 좌표 2개씩 2개가 한줄로 사각형 두개가 주어짐
# 겹치는 부분을 확인하여 직사각형, 선분, 점, 안겹침을 구분하기
# 직사각형 : a, 선분 : b, 점 : c, 안겹침 : d
# 좌표값은 1이상 50000이하
# 사각형 1 : sx1, sy1, ex1, ey1
# 사각형 2 : sx2, sy2, ex2, ey2

N = 4
for i in range(N):
    sx1, sy1, ex1, ey1, sx2, sy2, ex2, ey2 = map(int, input().split())
    if sy1 > ey2 or ey1 < sy2 or sx1 > ex2 or ex1 < sx2: # 안겹침
        result = 'd'

    elif ex1 == sx2 or sx1 == ex2 : # 세로 일치
        if ey1 == sy2 or sy1 == ey2: # 가로 일치
            result = 'c' # 점
        else:
            result = 'b' # 변

    elif ey1 == sy2 or sy1 == ey2: # 세로 x, 가로 o
        result = 'b'
    else:
        result ='a'
    print(result)