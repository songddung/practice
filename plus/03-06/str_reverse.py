N = int(input())

for i in range(N):
    txt = input()
    reverse_txt = ''
    for j in range(len(txt)-1, -1, -1):
        reverse_txt += txt[j]
    print(reverse_txt)