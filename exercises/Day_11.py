#Q38:

def tpl_slice():
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    n1 = tpl[:5]
    n2 = tpl[5:]
    print(n1, n2)

tpl_slice()

#Q39:
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
li = []
for i in tpl:
    if i%2==0:
        li.append(i)

tpl2 = tuple(li)
print(tpl2)

#Q40:
def yes_not():
    q = input("Yes or No?: ")
    if q == 'Yes' or q == 'yes' or q == 'YES':
        print("Yes")
    else:
        print('No')

yes_not()