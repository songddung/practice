def solve():
    ar =[]
    for _ in range(5):
        ar.append(list(map(int,input().split())))
    check = []
    for _ in range(5):
        check.extend(list(map(int,input().split())))


    count = 0

    for n in range(25): # 부른 번호 인덱스 뽑기
        for i in range(5): # 행
            for j in range(5): # 열
                    num = check[n]  # 부른 번호
                    if ar[i][j] == num:  # ar리스트의 현재 인덱스가 부른 번호랑 맞을때까지 찾기
                        count += 1  # 부를때 마다 카운트 증가
                        ar[i][j] = 0
                        break
            else:
                continue
            break

        if count >= 12:
            result =0
            # 행 검사
            for r in range(5):
                col_check = 0
                for c in range(5):
                    if ar[r][c] == 0 :
                        col_check += 1
                    if col_check == 5:
                        result +=1
                    if result == 3:
                        # print('행')
                        return count

            ### 열 검사
            for c in range(5):
                row_check = 0
                for r in range(5):
                    if ar[r][c] == 0 :
                        row_check += 1
                    if row_check == 5:
                        result +=1
                    if result == 3:
                        # print('열')
                        return count

            ### 대각선 검사
            r_crs_check = 0
            crs_check = 0
            for p in range(5):
                if ar[p][p] == 0:
                    crs_check +=1
                if ar[p][5-p-1] == 0:
                    r_crs_check += 1

                if crs_check == 5:
                    result +=1
                if r_crs_check == 5:
                    result +=1
            if result == 3:
                # print('대각선')
                return count

print(solve())