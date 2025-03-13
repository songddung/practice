ar = ['A', 'B', 'C', 'D']
N = len(ar)


def get_sub(tar):
    # print(f'target = {tar}', end=' / ')
    for i in range(N):
        # 각 원소가 포함?
        if tar & 0x1:
            print(ar[i], end='')
        tar >>= 1


# 전체 부분 집합을 확인해야한다.
for t in range(1 << N):
    get_sub(t)
    print()

# ar = ['A', 'B', 'C', 'D']
# N = len(ar)
# result = 0
#
#
# def get_sub(tar):
#     global result
#     count = 0
#     for i in range(N):
#         if tar & 0x1:
#             count += 1
#         tar >>= 1
#     if count >= 2:
#         result += 1
#
#
# for t in range(1 << N):
#     get_sub(t)
#
# print(result)
