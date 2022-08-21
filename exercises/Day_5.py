#16:
def get_odd():
    raw = input('numbers: ').split(',')
    lst = []
    raw = [int(i) for i in raw]
    for i in raw:
        if i %2 != 0:
            i = i* i
            lst.append(str(i))

    print(lst)

get_odd()

#Q17:
total = 0
while True:
    s = input().split()
    if not s:            # break if the string is empty
        break
    cm,num = map(str,s)    # two inputs are distributed in cm and num in string data type

    if cm=='D':
        total+=int(num)
    if cm=='W':
        total-=int(num)

print(total)