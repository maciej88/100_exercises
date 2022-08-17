#ex1
result = []
for i in range(2000, 3000+1): # +1 for clear number 3000
    if (i % 7 == 0) and (i %5 != 0):
        result.append(str(i))

print(','.join(result))

#ex2:
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(input("wpisz liczbę dla silni: "))
print(fact(x))

#ex3:
def get_dictionary():
    try:
        n = int(input('Enter number: '))
        d = dict()
        for i in range(1, n+1):
            d[i] = i *i
        return d
    except ValueError:
        print("that should be clear number not other!")

print(get_dictionary())