#Q90:
string = input('Give word: ')
dic = {}
for i in sorted(set(string)):
    print(f'{i}, {string.count(i)}')

#Q91:
x = input('another for reverse: ')
x = x[::-1]
print(x)