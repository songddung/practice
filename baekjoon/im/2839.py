# 설탕배달
# 5, 3 키로 봉지로 나누기
# 5로 나누고 몫+1 만큼 반복문 돌리기
#
# 나머지가 남으면 -1 리턴


N = int(input())

def solve(n):
    iter = n // 5 # 반복문을 돌릴 횟수
    mn = 5000
    for i in range(iter+1):
        count = i # 초기 5키로 봉지 수
        total = n - i*5 # 3키로 봉지로 나눌 무게
        if total % 3 != 0: # 3키로로 안나누어지면 다음으로 넘어가기
            continue
        three = total//3
        count += three

        if mn > count:
            mn = count
    if mn == 5000: # 정확하게 안나누어지면 -1 리턴
        return -1
    return mn

print(solve(N))