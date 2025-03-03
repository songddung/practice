# 킹
# 입력1 : 킹의 위치, 돌의 위치, 움직이는 횟수
# 움직이는 횟수만큼 반복문
# 이동을 문자로 줘서 딕셔너리 사용
# 출력 : 마지막 킹의 위치 , 마지막 돌의 위치


move = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (-1, 0),
    'T' : (1, 0),
    'RT' : (1, 1),
    'LT' : (1, -1),
    'RB' : (-1, 1),
    'LB' : (-1, -1),
}
row = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7
}

ar = [[0]*8 for _ in range(8)]
arr = []
king, stone, cnt = map(str, input().split())
king_p = (int(king[1])-1, row[king[0]])
stone_p = int(stone[1])-1, row[stone[0]]


for i in range(int(cnt)):
    arr.append(input())

for i in arr:
    dy, dx = king_p[0] + move[i][0],  king_p[1] + move[i][1]

    if 0 <= dy < 8 and 0 <= dx < 8:

        if stone_p == (dy, dx):
            py, px = stone_p[0] + move[i][0],  stone_p[1] + move[i][1]
            if 0 <= py < 8 and 0 <= px < 8:
                stone_p = (py, px)
                king_p = (dy, dx)
        else:
            king_p = (dy, dx)

def find_key(my_dict, target):
    for k, v in my_dict.items():
        if v == target:
            return k


king_p = find_key(row, king_p[1]) + str( (king_p[0]+1))
print(king_p)
stone_p = find_key(row, stone_p[1]) + str( (stone_p[0]+1))
print(stone_p)