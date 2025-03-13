coin_ar = [500, 100, 50, 10]
target = 1730
cnt = 0

for c in coin_ar:
    possible_cnt = target // c
    cnt += possible_cnt
    target -= possible_cnt*c

print(cnt)
print(15**15)