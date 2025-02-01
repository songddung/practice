ar = [1, 2, 3, 4, 4, 5]
bucket = [0] * (max(ar) + 1) # max값이 들어갈 자리의 인덱스가 max - 1 이기 때문

print(bucket)
for i in ar:
    bucket[i] += 1

print(bucket)