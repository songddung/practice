# 스위치 켜고 끄기
N = int(input())
ar = list(map(int, input().split()))
T = int(input())

for i in range(T):
    gen, num = map(int, input().split())

    idx = num - 1  # 0-base 인덱스


    # 남자일때
    if gen == 1:
        for i in range(idx, len(ar), num):
            if ar[i] == 1:
                ar[i] = 0
            else:
                ar[i] = 1


    # 여자일때
    if gen == 2:
        i = 1
        if ar[idx] == 1:
            ar[idx] = 0
        else:
            ar[idx] = 1
        while 0 <= idx-i and idx+i < len(ar) and ar[idx+i] == ar[idx-i]:
            if ar[idx+i] == 1:
                ar[idx + i] = 0
                ar[idx - i] = 0
            else:
                ar[idx + i] = 1
                ar[idx - i] = 1
            i += 1

print(ar)