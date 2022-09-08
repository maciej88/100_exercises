import itertools

#Q90:
string = input('Give word: ')
dic = {}
for i in sorted(set(string)):
    print(f'{i}, {string.count(i)}')

#Q91:
x = input('another for reverse: ')
x = x[::-1]
print(x)

#Q92:
x = input('another for reverse: ')
x = x[::2]
print(x)

#Q93:
print(list(itertools.permutations([1, 2, 3])))

#Q94:
def answer(head, legs):
    if head*2 == legs:
        return print(f"Chickens: {head}, no rabbits")
    elif head*2 <= legs:
        result = legs - (head*2)
        rabbits = result/2
        chickens = (head) - rabbits
        return print(f'chickens: {int(chickens)}, rabbits: {int(rabbits)}')

answer(35, 94)
