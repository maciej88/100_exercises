#Q90:
string = input('Give word: ')
dic = {}
for i in sorted(set(string)):
    print(f'{i}, {string.count(i)}')