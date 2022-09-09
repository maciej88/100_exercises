import textwrap
import string

#Q95:
x = int(input("Score: "))
i = map(int, input("scores: ").split())
i = list(set(i))
i.sort()
print(i[-2])

#Q96:
s = input("String to wrap: ")
w = int(input("number of letters in wrap: "))
dspl = textwrap.wrap(s, w)
for i in dspl:
    print(i)

#Q97:
def rangoli():
    n = int(input("Size: "))
    alpha = string.ascii_lowercase
    w = 4*n - 3
    r = []
    for i in range(n):
       part = '-'.join(alpha[n-i - 1:n])
       mid = part[-1:0:-1] + part
       result = mid.center(w, '-')
       r.append(result)
    if len(r) > 1:
        for i in r[n - 2::-1]:
            r.append(i)
    r = '\n'.join(r)
    print(r)

rangoli()