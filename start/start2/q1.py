hex = {'0' : 0,
       '1' : 1,
      '2' : 2,
      '3' : 3,
      '4' : 4,
      '5' : 5,
      '6' : 6,
      '7' : 7,
      '8' : 8,
      '9' : 9,
      'A' : 10,
      'B' : 11,
      'C' : 12,
      'D' : 13,
      'E' : 14,
      'F' : 15
    }

ar = ['0', 'F', '9', '7', 'A', '3']
txt = ''
for i in ar:
    tx = str(bin(hex[i])[2:])
    if len(tx) < 4:
        for i in range(4-len(tx)):
            tx = '0' + tx
    txt += tx

for i in range(0, len(txt), 7):
    result = '0b'+txt[i:i+7]
    print(int(result, 2))

