# # arr = []
# # select = []
# # select_num = []
# # L = int(input())
# # for i in range(L) :
# #     arr.append(0)
# # N = int(input())


# # for i in range(1, N+1) :
    
# #     select = list(map(int, input().split()))
  
# #     if i == 1 :
# #         for j in range(select[0],select[1]+1):
# #             arr[j-1] = i
# #     else :
# #         for k in range(select[0], select[1]+1) :
# #             if arr[k-1] == 0 :
# #                 print(f'k:{k}')
# #                 arr[k-1] = i
# #                 print(arr)
# #             else :
# #                 continue
# #     select_num.append(select)




# # index_num = []
# # # 많이 받은 사람
# # # select_num 리스트에 각 번호를 세서
# # # 가장 많은사람 동점이 있을 경우 인덱스가 낮은 사람
# # index1 = 0
# # for z in range(1, N+1) :

# #     pass

# # # 많이 받을줄 알았던 사람
# # # select_num 리스트에 하나씩 뽑아서 뒷번호에서 앞번호를 빼고 가장 큰사람
# # # 동점이 있을 경우 인덱스가 낮은 사람
# # prediction = []
# # index2 = 0
# # for i in range(N) :
# #     pass

# # ar = [1, 2, 3, 4, 4, 5]
# # bucket = [0] * (max(ar) + 1) # max값이 들어갈 자리의 인덱스가 max - 1 이기 때문


# # for i in ar:
# #     bucket[i] += 1

# # print(bucket)

# a = 1*1e10000
# print(a)




# import sys

# print(sys.maxsize)

# print(True + False)



# print(9 + 9 * 9 + 9*9*9 + 9*9*9*9)

# num = int(input())
# ar = [1, 11, 111, 1111]
# result = 0

# for i in ar :
#     result += num * i
# print(result)

# a = 'aaa'
# print(id(a.upper()))

# print(id(a))
# # print(new_a)
# print('A'+32)

# print(''.join([chr(ord(ch)+ 10) for ch in 'Hello']))

# chr()

# ar = list(map(int, input().split()))
# print(ar)

# ar = [1,2,3,4,5]
# expression = [[i] for i in ar if i % 2 == 0]
# print(expression)

# data1 = [[0]*10 for i in range(10)]
# print(data1)

# data2 = [ [0 for i in range(10)] for j in range(10)]
# print(data2)

# a = tuple()
# b = (1,)

# print(len(a))
# print(len(b))

# arr = [0]*5
# print(arr)

# text = 'aaa'
# print(text.lower())

# dc = {'a' : 1, 'b' : 2}
# dc.pop('a')
# print(dc)


# st = set()
# st2 = st.copy()
# print(st2)

# ar = [1,2,3,4]
# print(ar[::-1])
# print(ar[1:-2])


# text = 'a1a2a3a4a56a7a8'

# def sum_of_text(txt):
#     total = 0 
#     for v in txt:
#         if '0' <= v <= '9':
#             total += ord(v)- ord('0')
#             print(ord(v), ord('0'))
#     return total

# result = sum_of_text(text)
# print(result)

# ar = ['a','a','b','b','b','c',1,1,1,1,2,3,3]
# my_dict = {}
# for i in ar :
#     my_dict[str(i)] = ar.count(i)
    
# print(my_dict)

# ar = [1,1,1,2,2,3,4,5,6,6,6,7,8]
# my_dict2 = {}
# for j in ar :
#     my_dict2[str(j)] = ar.count(j)
# print(my_dict2)

# print(''.join([chr(ord(ch)+10)for ch in 'asong']))
# result = ''
# num = 9
# while True :
#     m = num // 2    
#     a = num % 2
#     result = str(a) + result
#     num = m
#     if m == 0:
#         break


# print(result[::-1])
# num = 9
# aaa = bin(num)[2:]
# print(aaa)

# def fibonacci(n):
#     fib_sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_sequence.append(a)
#         a, b = b, a + b
#     return fib_sequence

# # 예시: 처음 10개의 피보나치 수열 출력
# print(fibonacci(10))


# ar = [[0] * i for i in range(10) ]
# print(ar)


