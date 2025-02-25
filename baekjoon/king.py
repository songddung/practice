### king (1063)

# 8 * 8 체스판
# 알파벳은 행 , 숫자는 열
# 입력 : 킹의 위치, 돌의 위치 , 움직이는 횟수
# 킹이 돌의 위치로 이동 시 킹이 움직인 것 처럼 돌도 움직이기
# 킹이나 돌이 체스판 밖으로 나갈 경우, 해당 움직임 무시

 
# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로


### 출력 킹과 돌의 위치 구하기


row  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
column = ['1', '2', '3', '4', '5', '6', '7', '8']

input1 = list(map(str, input().upper().split())) # 위치와 이동 횟수
input2 = []
for i in range(int(input1[2])) :
    input2.append(input().upper()) # 이동

# print(input1)
# print(input2)
# print(column.index(input1[0][0]))
# print(row.index(input1[0][1]))

### 이동 규칙
move = {
    'R' : [1, 0],
    'L' : [-1, 0],
    'B' : [0, -1],
    'T' : [0, 1],
    'RT' : [1, 1],
    'LT' : [-1, 1],
    'RB' : [1, -1],
    'LB' : [-1, -1]
}



### 초기 위치 설정


king = [row.index(input1[0][0]), column.index(input1[0][1])]
stone = [row.index(input1[1][0]), column.index(input1[1][1])]



### 위치 이동
for i in input2 :
    move_x = move[i][0]
    move_y = move[i][1]




    # 킹의 새로운 위치
    new_king_x = king[0] + move_x
    new_king_y = king[1] + move_y

    ### 장외 시 넘기기
    if new_king_x < 0 or new_king_x > 7 or new_king_y < 0 or new_king_y > 7:
        continue




    ### 킹과 돌이 겹칠 경우
    if new_king_x == stone[0] and new_king_y == stone[1] :
        new_stone_x = stone[0] + move_x
        new_stone_y = stone[1] + move_y




        ### 새로운 돌위치 확인
        if new_stone_x < 0 or new_stone_x > 7 or new_stone_y < 0 or new_stone_y > 7:
            continue


        stone[0] = new_stone_x
        stone[1] = new_stone_y



    ### 킹 이동
    king[0] = new_king_x
    king[1] = new_king_y

print(f'{row[king[0]]}{column[king[1]]}')
print(f'{row[stone[0]]}{column[stone[1]]}')








