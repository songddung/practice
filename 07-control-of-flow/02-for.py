items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)

country = 'Korea'

for char in country :
    print(char)

my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for k in my_dict :
    print(k)
    print(my_dict[k])


numbers = [4, 6, 10, -8, 5]
for i in range(len(numbers)) :
    numbers[i] = numbers[i] * 2

print(numbers)  # [8, 12, 20, -16, 10]


outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
"""
??
"""


elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)  # ['A', 'B'] ['c', 'd']

for elem in elements:
    for item in elem:
        print(item)  # A B c d
