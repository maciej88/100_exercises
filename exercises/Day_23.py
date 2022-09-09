import textwrap

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