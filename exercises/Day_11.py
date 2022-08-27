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

#Q41:
def sqrs(item):
    return item ** 2


lst = [i for i in range(1, 11)]
print(list(map(sqrs, lst)))

#Q42:
def even(x):
    return x%2==0

def squer(x):
    return x*x

li = [1,2,3,4,5,6,7,8,9,10]
li = map(squer,filter(even,li))   # first filters number by even number and the apply map() on the resultant elements
print(list(li))

#Q43:
def even(x):
    return x%2==0

evenNumbers = filter(even, range(1,21))
print(list(evenNumbers))