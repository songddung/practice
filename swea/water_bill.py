# A사 리터당 P원
# B사 기본요금 Q원 , R리터 이하 기본요금, R보다 많은 경우 리터당 S원 추가
# 한달에 W리터 쓰면?

T = int(input())

def solve():
    P, Q, R, S, W = map(int, input().split())
    if W < R: # 사용량이 기본제공량 보다 작으면
        b_bill = Q
        a_bill = W * P
        if b_bill < a_bill:
            return b_bill
        else:
            return  a_bill
    else:
        a_bill = W * P
        b_bill = Q + -(R-W)*S
        if b_bill < a_bill:
            return b_bill
        else:
            return a_bill

for t in range(1, T+1):
    print(f'#{t} {solve()}')