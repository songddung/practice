# def seq_search(a, n, key):
#     for i in range(n):
#         if a[i] == key:
#             return i
#     return -1
#
#
# arr = [4, 9, 11, 23, 2, 19, 7]
# print(seq_search(arr, len(arr), 8))
#
# key = 11
# ans = -1
# for i in range(len(arr)):
#     if arr[i] == key:
#         ans = i
# print(ans)
#
#
# arr = [[1,2,3],[4,5,6][7,8,9]]
#
# N = 3
# key = 5
# ans = 0 # key가 있으면 1, 없으면 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == key:
#             ans = 1
#             break

def solve(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start+end)//2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1