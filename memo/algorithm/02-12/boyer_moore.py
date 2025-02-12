#tp를 이동한다.
def BM(t, p):
    N = len(t)
    M = len(p)

    jump = [M] * (ord('z') + 1)
    for i in range(M):
        idx = ord(p[i])
        jump[idx] = M-1-i

    print(jump[ord('r')])
    print(jump[ord('m')])

    tp = pp = 0
    while tp < N and pp >= 0:
        if t[tp] == p[pp]:
            tp -= 1
            pp -= 1
        else:
            idx = ord(t[tp])
            tp += jump[idx]
            pp = M - 1
    if pp == 1:
        return tp+1

t = 'a pattern matching algorithm'
p = 'rithm'
print(BM(t, p))

p = 'a pa'
print(BM(t, p))

p = 'match'
print(BM(t, p))