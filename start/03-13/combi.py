# 조합
#
# N = int(input())
# M = int(input())
#
# num1 = N
# num2 = N-M
# num3 = M
#
# for i in range(N-1,0,-1):
#     num1 *= i
#
#
# for j in range(N-M-1, 0, -1):
#     num2 *= j
#
#
# for k in range(M-1, 0, -1):
#     num3 *= k
#
# result = num1 // (num2*num3)
# print(result)
#
# # 조합식 뽑기
# ar = ['A', 'B', 'C', 'D', 'E']
# n = 3
# path = []
#
#
# def recur(cnt, start):
#     if cnt == n:
#         print(*path)
#         return
#
#     for i in range(start, len(ar)):
#         path.append(ar[i])
#         recur(cnt + 1, i + 1)
#         path.pop()
#
#
# recur(0, 0)

# 주사위 뽑기
import time

N = 3
ar = [1, 2, 3, 4, 5, 6]
path = []
result = 0


def recur(cnt, start):
    global result
    if cnt == 3:
        print(path)
        result += 1
        return

    for i in range(start, 7):
        path.append(i)
        recur(cnt + 1, i)
        path.pop()


start = time.time()
recur(0, 1)
end = time.time()
print(f'{end-start:.5f} sec')
print(result)